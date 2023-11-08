from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     
     path('', views.listar_preguntas, name='Inicio'),
     path("accounts/", include("django.contrib.auth.urls")),
     path('accounts/register/', views.register, name='register'),
     path('pregunta', views.crear_pregunta, name='Pregunta'),
      path('editar_pregunta/<int:pregunta_id>/', views.editar_pregunta, name='editar_pregunta'),
      path('borrar_pregunta/<int:pregunta_id>/', views.borrar_pregunta, name='borrar_pregunta'),
     path('foro', views.listar_preguntas, name='Foro'),
     path('proyectos', views.proyectos, name='Proyectos'),
]
