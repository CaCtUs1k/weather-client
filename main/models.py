from django.db import models

from user.models import User


class WeatherReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    city = models.CharField(max_length=63)
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
