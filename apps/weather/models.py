# weather/models.py
from django.db import models


class SearchHistory(models.Model):
    session_key = models.CharField(max_length=40)
    city = models.CharField(max_length=100)
    search_date = models.DateTimeField(auto_now=True)
    units = models.CharField(max_length=1, choices=[('C', 'Celsius'), ('F', 'Fahrenheit')], default='C')

    class Meta:
        unique_together = ('session_key', 'city')
        ordering = ['-search_date']

    def __str__(self):
        return f"{self.city} - {self.search_date}"
