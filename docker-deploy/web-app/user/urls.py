from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/driver', views.register_driver_view, name='register_driver'),
    path('revise_info', views.revise_car_view, name='revise_info'),
]