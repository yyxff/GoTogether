from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import RegisterForm, LoginForm
from django.views.decorators.http import require_http_methods
from .models import RSSUser

# Create your views here.
@require_http_methods(['GET', 'POST'])
def register_view(request):
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
            print(form.errors.get_json_data())
            return redirect('user:register')

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
                return redirect('/')
            else:
                form.add_error('username', 'Username or password error.')
                return render(request, 'user/login.html', context={'form' : form, 'form_error': form.errors.get_json_data()})

def logout_view(request):
    user = RSSUser.objects.first()
    if user.is_authenticated:
        request.session.flush()
        return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))

def register_driver_view(request):
    return redirect(reverse('index'))