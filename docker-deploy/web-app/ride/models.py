from django.db import models

# Create your models here.

class RideModel(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival_time = models.DateTimeField(auto_now_add=False)
    total_passenger = models.IntegerField(default=1)
    can_share = models.BooleanField(default=False)
    vehicle_type = models.CharField(blank=True, default='')
    sp_info = models.TextField(blank=True, default='')
    is_confirmed = models.BooleanField(default=False)

