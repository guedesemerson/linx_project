from rest_framework import serializers
from weather.models import Weather


class SearchWeatherSerializer(serializers.ModelSerializer):
    weather_date = serializers.DateField(write_only=True)

    class Meta:
        model = Weather
        fields = (
            'id',
            'city',
            'country',
            'weather_object',
            'weather_date'
        )
        read_only_fields = [
            'id',
            'country',
            'weather_object',
        ]


class ListWeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = (
            'id',
            'city',
            'country',
            'weather_object',
        )
        read_only_fields = [
            'id',
        ]
