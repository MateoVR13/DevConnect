from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
     
     path('', views.foro, name='Inicio'),
     path('foro', views.foro, name='Foro'),
     path('login', views.user_login, name='Login'),
     path('register', views.register, name='Register'),
     path('proyectos', views.proyectos, name='Proyectos'),
     path('logout/', LogoutView.as_view(), name='logout'),
]
