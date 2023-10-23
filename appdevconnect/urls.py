from django.urls import path
from . import views

urlpatterns = [
     
     path('', views.inicio, name='inicio'),
     path('foro', views.foro, name='Foro'),
     path('repositorio', views.repositorio, name='Repositorio'),
]
