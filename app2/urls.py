# app2/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_app2'),
    path('services/', views.services, name='services_app2'),
    path('team/', views.team, name='team_app2'),
]
