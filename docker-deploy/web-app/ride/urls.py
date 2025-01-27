from django.urls import path
from . import views
from RSS.views import index_view
app_name = 'ride'

urlpatterns = [
    path('new/', views.new_ride_view, name='new_ride'),
    path('view/', views.my_ride_view, name='view_my_ride'),
    path('revise/<int:ride_id>', views.revise_ride_info, name='revise_ride'),
    path('search/my/', views.search_my_ride, name='search_my_ride'),
    path('detail/<int:ride_id>', views.ride_detail_view, name='ride_detail'),
    path('delete/<int:ride_id>', views.ride_delete_view, name='delete_ride'),
    path('share/', views.share_ride_view, name='view_share_ride'),
    path('search/share/', views.search_share_ride, name='search_share_ride'),
    path('requests/', views.ride_requests_view, name='ride_requests'),
    path('requests/accept/<int:ride_id>', views.ride_info_view, name='ride_info'),
    path('requests/search', views.search_ride_request, name='search_ride_request'),
]