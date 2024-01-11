import os

import requests


def response_api_current_weather(city):
    api_key = os.getenv('API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    return requests.get(url)


def response_api_weekly_weather(city):
    api_key = os.getenv('API_KEY')
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7'
    return requests.get(url)


def response_api_hourly_weather(city):
    api_key = os.getenv('API_KEY')
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=10'
    return requests.get(url)
