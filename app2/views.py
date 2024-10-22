# app2/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'app2/home.html')

def services(request):
    return render(request, 'app2/services.html')

def team(request):
    return render(request, 'app2/team.html')
