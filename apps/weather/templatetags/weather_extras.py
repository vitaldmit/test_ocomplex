from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def index(indexable, i):
    return indexable[i]


@register.filter
def range(value):
    return range(value)


@register.filter
def weather_icon(weathercode):
    icons = {
        0: "☀️",  # Clear sky
        1: "🌤️",  # Mainly clear
        2: "⛅",  # Partly cloudy
        3: "☁️",  # Overcast
        45: "🌫️",  # Fog
        48: "🌫️",  # Depositing rime fog
        51: "🌧️",  # Light drizzle
        53: "🌧️",  # Moderate drizzle
        55: "🌧️",  # Dense drizzle
        61: "🌦️",  # Slight rain
        63: "🌧️",  # Moderate rain
        65: "🌧️",  # Heavy rain
        71: "🌨️",  # Slight snow fall
        73: "🌨️",  # Moderate snow fall
        75: "🌨️",  # Heavy snow fall
        77: "🌨️",  # Snow grains
        80: "🌦️",  # Slight rain showers
        81: "🌧️",  # Moderate rain showers
        82: "🌧️",  # Violent rain showers
        85: "🌨️",  # Slight snow showers
        86: "🌨️",  # Heavy snow showers
        95: "⛈️",  # Thunderstorm
        96: "⛈️",  # Thunderstorm with slight hail
        99: "⛈️",  # Thunderstorm with heavy hail
    }
    return mark_safe(icons.get(weathercode, "❓"))
