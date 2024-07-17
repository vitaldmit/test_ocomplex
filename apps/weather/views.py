import requests
from django.shortcuts import render
from .models import SearchHistory
from django.db.models import Count

def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_url = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true"
        response = requests.get(api_url)
        weather_data = response.json()

        # Сохраняем поиск в истории
        SearchHistory.objects.create(user=request.user if request.user.is_authenticated else None, city=city)

        context = {
            'city': city,
            'temperature': weather_data['current_weather']['temperature'],
            'windspeed': weather_data['current_weather']['windspeed'],
        }
        return render(request, 'weather/result.html', context)

    # Получаем последний поиск пользователя
    last_search = None
    if request.user.is_authenticated:
        last_search = SearchHistory.objects.filter(user=request.user).order_by('-search_date').first()

    return render(request, 'weather/search.html', {'last_search': last_search})

def search_stats(request):
    stats = SearchHistory.objects.values('city').annotate(count=Count('city')).order_by('-count')
    return render(request, 'weather/stats.html', {'stats': stats})
