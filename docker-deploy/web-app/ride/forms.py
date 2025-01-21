from click import style
from django import forms
from .models import RideModel

class NewRideForm(forms.ModelForm):
    class Meta:
        model = RideModel
        exclude = ['is_confirmed', 'owner', 'driver',]
        widgets = {
            'departure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter departure position'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter destination'}),
            'arrival_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter expected arrival time'}),
            'total_passenger': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter total number of passengers'}),
            'can_share': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left:2px; margin-top:6px;'}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter expected vehicle type (Optional)'}),
            'sp_info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter special requirements (Optional)', 'style':'height:38px'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        is_confirmed = cleaned_data.get('is_confirmed')
        if is_confirmed:
            raise forms.ValidationError('You cannot revise a confirmed ride.')
        else:
            return cleaned_data