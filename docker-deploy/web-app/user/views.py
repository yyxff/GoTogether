from http.client import responses

from django.contrib.auth import login, logout
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import RegisterForm, LoginForm, DriverRegisterForm, CarForm
from django.views.decorators.http import require_http_methods
from .models import RSSUser, CarModel

# Create your views here.
@require_http_methods(['GET', 'POST'])
def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'user/register.html', context=context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('pwd2')
            RSSUser.objects.create_user(username=username, password=password)
            return redirect(reverse('user:login'))
        else:
            return redirect(reverse('user:register'))

@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', context={'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('pwd')
            remember = form.cleaned_data.get('remember')
            user = RSSUser.objects.filter(username=username).first()
            if user and user.check_password(password):
                # login
                login(request, user)
                # if not remember
                if not remember:
                    request.session.set_expiry(0)
                return redirect(reverse('index'))
            else:
                form.add_error('username', 'Username or password error.')
                return render(request, 'user/login.html', context={'form' : form, 'form_error': form.errors.get_json_data()})

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

@require_http_methods(['GET', 'POST'])
def register_driver_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('user:login'))
    if request.method == 'GET':
        form = DriverRegisterForm()
        return render(request, 'user/driver_register.html', context={'form': form})
    else:
        form = DriverRegisterForm(request.POST)
        if form.is_valid():
            # get post data
            vehicle_type = form.cleaned_data.get('vehicle_type')
            vehicle_number = form.cleaned_data.get('vehicle_number')
            max_passenger = form.cleaned_data.get('max_passenger')
            sp_info = form.cleaned_data.get('sp_info')

            # TODO: Model and ForeignKey
            # get user
            user = request.user

            # set user info
            user.is_driver = True
            cars = CarModel.objects.create(user=user,
                                    vehicle_type=vehicle_type,
                                    vehicle_number=vehicle_number,
                                    max_passenger=max_passenger,
                                    sp_info=sp_info)
            user.save()
            return redirect(reverse('index'))
        else:
            form_error = form.errors.get_json_data()
            return render(request, 'user/driver_register.html', context={'form': form, 'form_error': form_error})

@require_http_methods(['GET', 'POST'])
def revise_car_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('user:login'))
    CarFormSet = modelformset_factory(CarModel,
                                      form=CarForm,
                                      fields=('vehicle_type', 'vehicle_number', 'max_passenger', 'sp_info'),
                                      extra=0)
    cars = CarModel.objects.filter(user=request.user)
    if request.method == 'GET':
        formset = CarFormSet(queryset=cars)
        return render(request, 'user/user_info.html', context={'forms': formset})
    else:
        formset = CarFormSet(request.POST, queryset=cars)
        if formset.is_valid():
            formset.save()
            return render(request, 'user/user_info.html', context={'forms': formset, 'is_success': True})
        else:
            return render(request, 'user/user_info.html', context={'forms': formset, 'is_success': False})