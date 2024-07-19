from django.urls import path
from .views import home, city_autocomplete, CitySearchCountView

urlpatterns = [
    path('', home, name='home'),
    path('city-autocomplete/', city_autocomplete, name='city_autocomplete'),
    path('api/city-search-count/', CitySearchCountView.as_view(), name='city_search_count'),
]
