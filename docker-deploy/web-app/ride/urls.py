from django.urls import path
from . import views
from RSS.views import index_view
app_name = 'ride'

urlpatterns = [
    path('new/', views.new_ride_view, name='new_ride'),
    path('view/', views.ride_view, name='view_ride'),
    path('revise/<int:ride_id>', views.revise_ride_info, name='revise_ride'),
    path('search/my/', views.search_my_ride, name='search_my_ride'),
    path('detail/<int:ride_id>', views.ride_detail_view, name='ride_detail'),
]