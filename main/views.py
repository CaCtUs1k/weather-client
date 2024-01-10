from django.shortcuts import render

from main.models import WeatherReport


def get_last_requests(request):
    logs = WeatherReport.objects.order_by('-timestamp')[:5]
    return render(request, 'weather_app/last_requests.html', {'logs': logs})
