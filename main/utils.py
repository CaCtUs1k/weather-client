import os

import requests


def response_api_current_weather(city):
    api_key = os.getenv("API_KEY")
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    return response


def response_api_weekly_weather(city):
    api_key = os.getenv("API_KEY")
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7'
    response = requests.get(url)
    return response

