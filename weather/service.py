import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast/?'
API_KEY = '401df1ecde76725239ec84925cbd8914'


def get_weather_info(city_name: str) -> dict:
    params = {
        'q': city_name,
        'appid': API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()
