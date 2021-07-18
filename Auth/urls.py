from django.urls import path
from . import views


urlpatterns = [    
    path('', views.responses.login_page, name='login_page'),
    path('login', views.responses.login_page, name='login_page'),
    path('dashboard', views.responses.dashboard_page, name='dashboard_page'),
    path('history', views.responses.history_page, name='history_page'),
    path('pricing', views.responses.pricing_page, name='pricing_page'),
    path('parked', views.responses.parked_page, name='parked_page'),
    path('users', views.responses.user_page, name='user_page'),
]
