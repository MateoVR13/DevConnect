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
     path('responder_pregunta/<int:pregunta_id>/', views.responder_pregunta, name='responder_pregunta'),
     path('registrar_proyecto/', views.registrar_proyecto, name='registrar_proyecto'),
     path('proyectos_alfabetico/', views.proyectos_alfabetico, name='proyectos_alfabetico'),
     path('proyectos_recientes/', views.proyectos_recientes, name='proyectos_recientes'),
     path('proyectos_antiguos/', views.proyectos_antiguos, name='proyectos_antiguos'),
     path('preguntas_alfabetico/', views.preguntas_alfabetico, name='preguntas_alfabetico'),
     path('preguntas_recientes/', views.preguntas_recientes, name='preguntas_recientes'),
     path('preguntas_antiguos/', views.preguntas_antiguos, name='preguntas_antiguos'),
     path('foro', views.listar_preguntas, name='Foro'),
     path('proyectos', views.listar_proyectos, name='Proyectos'),
     path('enciclopedia', views.enciclopedia, name='Enciclopedia'),
]
