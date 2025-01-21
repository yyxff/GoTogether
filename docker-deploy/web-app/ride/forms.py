from django import forms
from .models import RideModel

class NewRideForm(forms.ModelForm):
    class Meta:
        model = RideModel
        exclude = ['is_confirmed', 'owner', 'driver',]