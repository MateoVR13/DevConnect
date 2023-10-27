from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.

def foro(request):
    return render(request, 'paginas/paginaForo.html')

def proyectos(request):
    return render(request, 'paginas/paginaProyectos.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Foro') 
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registro.html', {'form': form})
