from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from weather.serializers import (
    SearchWeatherSerializer,
    ListWeatherSerializer
)
from weather.service import get_weather_info
from weather.models import Weather
from weather.utils import filter_weather_by_date


class SearchWeatherView(GenericAPIView):
    serializer_class = SearchWeatherSerializer

    def post(self, request):
        city = request.data['city']
        date = request.data['weather_date']

        response_weather = get_weather_info(city)

        if response_weather['cod'] == '404' or response_weather['cod'] == '400':
            return Response({"city": "insert a city/existent city"})

        weather_filtered = filter_weather_by_date(date, response_weather['list'])

        if not weather_filtered:
            return Response({"Date": "There is no weather for your date."})

        if response_weather['cod'] == '200':

            city = response_weather['city']['name']
            country = response_weather['city']['country']
            weather = weather_filtered

            Weather.objects.create(
                city=city,
                country=country,
                weather_object=weather
            )
            return Response({
                'city': city,
                'country': country,
                'weather_object': weather_filtered
            },
                status=status.HTTP_200_OK
            )

        return Response(response_weather)


class ListWeatherView(ListAPIView):
    serializer_class = ListWeatherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']

    def get_queryset(self):
        return Weather.objects.all()


