from django.shortcuts import render
import os


# Create your views here.
def login_page(request):
    return render(request, 'Auth/index.html')

def dashboard_page(request):
    return render(request, 'Auth/dashboard.html')

def all_vehicle_page(request):
    return render(request, 'Auth/all_vehicle.html')

def pricing_page(request):
    return render(request, 'Auth/pricing.html')

def today_page(request):
    return render(request, 'Auth/today.html')

def user_page(request):
    return render(request, 'Auth/user.html')