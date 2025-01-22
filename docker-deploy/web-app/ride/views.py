from traceback import print_tb

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .forms import NewRideForm
from django.views.decorators.http import require_http_methods
from .models import RideModel
# Create your views here.

@require_http_methods(['GET', 'POST'])
def new_ride_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('user:login'))
    if request.method == 'GET':
        form = NewRideForm()
        return render(request, 'ride/new_ride.html', context={'form': form})
    else:
        form = NewRideForm(request.POST)
        if form.is_valid():
            departure = form.cleaned_data.get('departure')
            destination = form.cleaned_data.get('destination')
            arrival_time = form.cleaned_data.get('arrival_time')
            total_passenger = form.cleaned_data.get('total_passenger')
            can_share = form.cleaned_data.get('can_share')
            vehicle_type = form.cleaned_data.get('vehicle_type')
            sp_info = form.cleaned_data.get('sp_info')
            owner = request.user

            RideModel.objects.create(departure=departure,
                                     destination=destination,
                                     arrival_time=arrival_time,
                                     total_passenger=total_passenger,
                                     can_share=can_share,
                                     vehicle_type=vehicle_type,
                                     sp_info=sp_info,
                                     owner=owner)
            return render(request, 'ride/new_ride.html', context={'form': form, 'success': True})
        else:
            return render(request, 'ride/new_ride.html', context={'form': form, 'success': False})

@login_required(login_url='/user/login/')
def ride_view(request):
    rides = RideModel.objects.filter(owner__exact=request.user)
    return render(request, 'ride/ride.html', context={'my_rides':rides})

# TODO: add a view for share ride form
@login_required(login_url='/user/login/')
@require_http_methods(['GET', 'POST'])
def revise_ride_info(request, ride_id):
    ride = RideModel.objects.get(pk=ride_id)
    form = NewRideForm(instance=ride)
    if request.method == 'GET':
        return render(request, 'ride/revise_ride.html', context={'form': form, 'ride': ride})
    else:
        form = NewRideForm(request.POST, instance=ride)
        if form.is_valid():
            form.owner = request.user
            form.save()
            return render(request, 'ride/revise_ride.html', context={'form': form, 'success': True})
        else:
            return render(request, 'ride/revise_ride.html', context={'form': form, 'success': False})
