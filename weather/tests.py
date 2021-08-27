from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestAppointmentAPI(APITestCase):

    def test_list_weather(self):
        response = self.client.get(
            reverse('api-weather:list_weather'),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_weather(self):
        response = self.client.post(
            reverse('api-weather:search_weather'),
            data={
                'city': 'Rio de Janeiro',
                'weather_date': "2021-08-30",
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


