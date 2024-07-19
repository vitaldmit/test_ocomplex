from rest_framework import serializers
from .models import SearchHistory


class CitySearchCountSerializer(serializers.Serializer):
    city = serializers.CharField()
    count = serializers.IntegerField()
