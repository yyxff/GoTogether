from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class RSSUser(AbstractUser):
    is_driver = models.BooleanField(default=False)
    vehicle_type = models.CharField(max_length=100, blank=True)
    vehicle_number = models.CharField(max_length=100, blank=True)
    max_passenger = models.IntegerField(blank=True, default=0)
    sp_info = models.CharField(blank=True)

