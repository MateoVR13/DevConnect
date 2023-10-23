from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def inicio(request):
    return HttpResponse("<h1>Bienvenido a DevConnect</h1>")

def foro(request):
    return render(request, 'paginas/landingPage.html')

def repositorio(request):
    return render(request, 'paginas/projectsPage.html')