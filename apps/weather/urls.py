from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city-autocomplete/', views.city_autocomplete, name='city_autocomplete'),
]
