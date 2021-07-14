from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('dashboard.html', views.dashboard_page, name='dashboard_page'),
    path('all_vehicle.html', views.all_vehicle_page, name='all_vehicle_page'),
    path('pricing.html', views.pricing_page, name='pricing_page'),
    path('pricing.html', views.pricing_page, name='pricing_page'),
    path('today.html', views.today_page, name='today_page'),
    path('user.html', views.user_page, name='user_page'),
]
