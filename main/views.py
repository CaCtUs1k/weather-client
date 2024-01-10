from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv

from main.models import WeatherReport
from main.utils import response_from_weather_api

load_dotenv()


def get_last_requests(request):
    logs = WeatherReport.objects.order_by('-timestamp')[:5]
    return render(request, 'weather_app/last_requests.html', {'logs': logs})


def get_current_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        response = response_from_weather_api(city)
        if response.status_code == 200:
            weather_info = response.json()
            report = WeatherReport(user=request.user, city=city, type="Current weather", information=weather_info)
            report.save()
            return render(request, 'weather_app/current_weather.html', {'report': report})
        else:
            return HttpResponse('Failed to fetch weather data')

    return render(request, 'weather_app/weather_form.html')
