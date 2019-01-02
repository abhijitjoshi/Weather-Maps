from django.db import models
from django.contrib.postgres.fields import JSONField


class DirectionsData(models.Model):
    origin = models.TextField(null=False, blank=False)
    destination = models.TextField(null=False, blank=False)
    travel_mode = models.TextField(null=False, blank=False, default='driving')
    routes_response = JSONField(blank=False, null=False, default=list([]))
    route_weather_data = JSONField(blank=True, null=True, default=list([]))
    route_cities_data = JSONField(blank=True, null=True, default=list([]))
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

