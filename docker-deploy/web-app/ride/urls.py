from django.urls import path
from . import views
app_name = 'ride'

urlpatterns = [
    path('new_ride', views.new_ride_view, name='new_ride'),
]