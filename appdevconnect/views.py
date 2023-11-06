from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm

def foro(request):
    return render(request, 'paginas/paginaForo.html')

def proyectos(request):
    return render(request, 'paginas/paginaProyectos.html')

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige al usuario a una página de confirmación o a donde desees
            return redirect('Foro')
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

