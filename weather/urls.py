from django.urls import path
from weather.views import (
    SearchWeatherView,
    ListWeatherView
)

app_name = "api-weather"

urlpatterns = [
    path('search_weather', SearchWeatherView.as_view(), name='search_weather'),
    path('list_weather', ListWeatherView.as_view(), name='list_weather'),
]