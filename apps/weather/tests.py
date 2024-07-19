import time
import json
from unittest.mock import patch

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

from .models import SearchHistory
from .views import get_weather, city_autocomplete


class WeatherProjectTestCase(TestCase):
    # def test_debug_setting(self):
    #     """Проверка, что DEBUG установлен в False для разработки"""
    #     self.assertFalse(settings.DEBUG)

    def test_installed_apps(self):
        """Проверка, что приложение 'apps.weather' установлено"""
        self.assertIn('apps.weather', settings.INSTALLED_APPS)

    def test_language_code(self):
        """Проверка, что язык установлен на русский"""
        self.assertEqual(settings.LANGUAGE_CODE, 'ru-RU')


class SearchHistoryModelTest(TestCase):
    def setUp(self):
        self.search_history = SearchHistory.objects.create(
            session_key='test_session_key',
            city='Москва',
            units='C'
        )

    def test_search_history_creation(self):
        """Проверка создания объекта SearchHistory"""
        self.assertTrue(isinstance(self.search_history, SearchHistory))
        self.assertEqual(str(self.search_history), f"Москва - {self.search_history.search_date}")

    def test_search_history_ordering(self):
        """Проверка сортировки по убыванию даты поиска"""
        SearchHistory.objects.all().delete()  # Clear existing objects

        SearchHistory.objects.create(
            session_key='test_session_key_2',
            city='Санкт-Петербург',
            units='C',
            search_date=timezone.now()
        )
        time.sleep(0.1)  # Небольшая задержка
        SearchHistory.objects.create(
            session_key='test_session_key_3',
            city='Москва',
            units='C',
            search_date=timezone.now()
        )

        searches = SearchHistory.objects.all()
        self.assertEqual(searches[0].city, 'Москва')
        self.assertEqual(searches[1].city, 'Санкт-Петербург')
        self.assertEqual(len(searches), 2)


class HomeViewTest(TestCase):
    @patch('apps.weather.views.requests.get')
    @patch('apps.weather.views.get_weather')
    def test_home_view_with_city(self, mock_get_weather, mock_get):
        """Проверка представления home с указанием города"""
        mock_get.return_value.json.return_value = {
            'results': [{'latitude': 55.7558, 'longitude': 37.6173, 'name': 'Москва', 'country': 'Russia'}]
        }
        mock_get.return_value.status_code = 200

        mock_get_weather.return_value = {
            'daily': {
                'time': ['2023-01-01'],
                'temperature_2m_max': [10],
                'temperature_2m_min': [5],
                'precipitation_sum': [0],
                'weathercode': [0]
            },
            'units': 'C'
        }

        response = self.client.get(reverse('home'), {'city': 'Москва'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/home.html')

    def test_home_view_without_city(self):
        """Проверка представления home без указания города"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/home.html')


class WeatherFunctionsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('apps.weather.views.requests.get')
    def test_get_weather(self, mock_get):
        """Проверка функции get_weather"""
        mock_get.return_value.json.return_value = {'daily': {'time': [], 'temperature_2m_max': [], 'temperature_2m_min': [], 'precipitation_sum': [], 'weathercode': []}}
        mock_get.return_value.status_code = 200

        result = get_weather(55.7558, 37.6173)
        self.assertIsNotNone(result)
        self.assertIn('daily', result)

    @patch('apps.weather.views.requests.get')
    def test_city_autocomplete(self, mock_get):
        """Проверка функции city_autocomplete"""
        mock_get.return_value.json.return_value = [{'display_name': 'Москва, Россия'}]
        mock_get.return_value.status_code = 200

        request = self.factory.get(reverse('city_autocomplete'), {'term': 'Москва'})
        response = city_autocomplete(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), ['Москва, Россия'])
