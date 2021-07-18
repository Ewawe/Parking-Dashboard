from django.urls import path
from . import views


urlpatterns = [
    path('login.html', views.login_page, name='login_page'),
    path('dashboard.html', views.dashboard_page, name='dashboard_page'),
    path('history.html', views.history_page, name='history_page'),
    path('pricing.html', views.pricing_page, name='pricing_page'),
    path('pricing.html', views.pricing_page, name='pricing_page'),
    path('parked.html', views.today_page, name='today_page'),
    path('user.html', views.user_page, name='user_page'),
]
