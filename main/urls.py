from django.urls import path

from main.views import get_current_weather

app_name = 'main'

urlpatterns = [
    path('current_weather/', get_current_weather, name='current-weather'),
]
