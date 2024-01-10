from django.urls import path

from main.views import get_last_requests, get_current_weather

app_name = 'main'

urlpatterns = [
    path('last_requests/', get_last_requests, name='last-requests'),
    path('current_weather/', get_current_weather, name='current-weather'),
]
