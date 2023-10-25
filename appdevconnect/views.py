from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def foro(request):
    return render(request, 'paginas/paginaForo.html')

def proyectos(request):
    return render(request, 'paginas/paginaProyectos.html')