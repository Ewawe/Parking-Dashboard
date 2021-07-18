from django.urls import path
from . import views


urlpatterns = [    
    path('', views.responses.login_page, name='login_page'),
    path('login.html', views.responses.login_page, name='login_page'),
    path('dashboard.html', views.responses.dashboard_page, name='dashboard_page'),
    path('history.html', views.responses.history_page, name='history_page'),
    path('pricing.html', views.responses.pricing_page, name='pricing_page'),
    path('parked.html', views.responses.parked_page, name='parked_page'),
    path('user.html', views.responses.user_page, name='user_page'),
]
