from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     
     path('', views.foro, name='Inicio'),
     path("accounts/", include("django.contrib.auth.urls")),
     path('accounts/register/', views.register, name='register'),
     path('foro', views.foro, name='Foro'),
     path('proyectos', views.proyectos, name='Proyectos'),
]
