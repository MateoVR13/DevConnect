from django.urls import path
from . import views

urlpatterns = [
     
     path('', views.foro, name='Inicio'),
     path('foro', views.foro, name='Foro'),
     path('registro', views.register, name='Registro'),
     path('proyectos', views.proyectos, name='Proyectos'),
]
