from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv

from main.utils import response_api_current_weather, response_api_weekly_weather

load_dotenv()


def get_current_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        response = response_api_current_weather(city)
        if response.status_code == 200:
            weather_info = response.json()
            return render(request, 'weather_app/current_weather.html', {'forecast': weather_info})
        else:
            return HttpResponse('Failed to fetch weather data')

    return render(request, 'weather_app/current_weather_form.html')


def get_weekly_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        response = response_api_weekly_weather(city)
        if response.status_code == 200:
            weather_info = response.json()
            return render(request, 'weather_app/weekly_weather.html', {'forecast': weather_info})
        else:
            return HttpResponse('Failed to fetch weather data')

    return render(request, 'weather_app/weekly_weather_form.html')
