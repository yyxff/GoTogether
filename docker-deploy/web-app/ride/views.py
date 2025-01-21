from django.shortcuts import render, redirect, reverse
from .forms import NewRideForm
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(['GET', 'POST'])
def new_ride_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('user:login'))
    form = NewRideForm()
    return render(request, 'ride/new_ride.html', context={'form': form})