from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv

from main.utils import response_from_weather_api

load_dotenv()


def get_current_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        response = response_from_weather_api(city)
        if response.status_code == 200:
            weather_info = response.json()
            return render(request, 'weather_app/current_weather.html', {'report': weather_info})
        else:
            return HttpResponse('Failed to fetch weather data')

    return render(request, 'weather_app/weather_form.html')
