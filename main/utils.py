import os

import requests


def response_from_weather_api(city):
    api_key = os.getenv("API_KEY")
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(url)
    return response

