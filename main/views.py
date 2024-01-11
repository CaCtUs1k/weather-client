from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv

from main.utils import (
    response_api_current_weather,
    response_api_weekly_weather,
    response_api_hourly_weather,
)

load_dotenv()


def get_current_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        response = response_api_current_weather(city)
        if response.status_code == 200:
            weather_info = response.json()
            return render(
                request,
                'weather_app/current_weather.html',
                {'forecast': weather_info},
            )
        else:
            return HttpResponse('Failed to fetch weather data')

    return render(request, 'weather_app/current_weather_form.html')


def get_weekly_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        response = response_api_weekly_weather(city)
        if response.status_code == 200:
            weather_info = response.json()
            return render(
                request,
                'weather_app/weekly_weather.html',
                {'forecast': weather_info},
            )
        else:
            return HttpResponse('Failed to fetch weather data')

    return render(request, 'weather_app/weekly_weather_form.html')


def get_hourly_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        date = request.POST.get('date')

        response = response_api_hourly_weather(city)
        if response.status_code == 200:
            weather_info = response.json()

            selected_day = None
            for day in weather_info['forecast']['forecastday']:
                if day['date'] == date:
                    selected_day = day
                    break

            return render(
                request,
                'weather_app/hourly_weather.html',
                {
                    'forecast': selected_day,
                    'city': city,
                    'date': date,
                },
            )
        else:
            return HttpResponse('Failed to fetch hourly weather data')

    return render(request, 'weather_app/hourly_weather_form.html')
