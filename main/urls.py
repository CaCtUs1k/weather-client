from django.urls import path

from main.views import get_last_requests

app_name = 'main'

urlpatterns = [
    path('last_requests/', get_last_requests, name='last-requests'),
]
