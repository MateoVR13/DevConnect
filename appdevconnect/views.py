from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PreguntaForm
from .models import Pregunta
from django.contrib.auth.decorators import login_required

from .forms import CustomRegistrationForm


def proyectos(request):
    return render(request, 'paginas/paginaProyectos.html')

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Foro')
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='accounts/login')
def crear_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            nueva_pregunta = form.save(commit=False)
            nueva_pregunta.user = request.user
            nueva_pregunta.save()
            return redirect('Foro')
    else:
        form = PreguntaForm()
    
    return render(request, 'createQuestion.html', {'form': form})

def listar_preguntas(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'paginas/paginaForo.html', {'preguntas': preguntas})

