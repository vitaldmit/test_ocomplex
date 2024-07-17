from django.test import TestCase, Client
from django.urls import reverse
from .models import SearchHistory

class WeatherViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_weather_view(self):
        response = self.client.get(reverse('get_weather'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/search.html')

    def test_search_stats_view(self):
        response = self.client.get(reverse('search_stats'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/stats.html')

    def test_search_history_creation(self):
        self.client.post(reverse('get_weather'), {'city': 'Moscow'})
        self.assertEqual(SearchHistory.objects.count(), 1)
        self.assertEqual(SearchHistory.objects.first().city, 'Moscow')
