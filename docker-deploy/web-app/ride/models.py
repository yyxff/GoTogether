from django.db import models
from user.models import RSSUser
# Create your models here.

class RideModel(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival_time = models.DateTimeField(auto_now_add=False, verbose_name='Expected arrival time')
    total_passenger = models.IntegerField(default=1)
    can_share = models.BooleanField(default=False, verbose_name='Shared ride')
    vehicle_type = models.CharField(blank=True, default='', verbose_name='Expected vehicle type*')
    sp_info = models.TextField(blank=True, default='', verbose_name='Special Needs*')
    is_confirmed = models.BooleanField(default=False)

    owner = models.ForeignKey(RSSUser, on_delete=models.CASCADE, related_name='owned_rides', default="")
    driver = models.ForeignKey(RSSUser, on_delete=models.CASCADE, related_name='confirmed_rides', default="")

