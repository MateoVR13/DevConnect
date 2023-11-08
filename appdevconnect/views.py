from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PreguntaForm, RespuestaForm
from .models import Pregunta, Respuesta
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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

@login_required(login_url='accounts/login')
def editar_pregunta(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)

    if request.method == 'POST':
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return redirect('Foro')

    else:
        form = PreguntaForm(instance=pregunta)

    return render(request, 'editQuestion.html', {'form': form, 'pregunta': pregunta})

@login_required(login_url='accounts/login')
def borrar_pregunta(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)

    if request.user == pregunta.user:
        pregunta.delete()
    
    return redirect('Foro')

def responder_pregunta(request, pregunta_id):
    pregunta = Pregunta.objects.get(id=pregunta_id)
    
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.question = pregunta
            respuesta.user = request.user
            respuesta.save()
            return redirect('Foro')
    else:
        form = RespuestaForm()

    return render(request, 'createAnswer.html', {'pregunta': pregunta, 'form': form})

