from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.

def foro(request):
    return render(request, 'paginas/paginaForo.html')

def proyectos(request):
    return render(request, 'paginas/paginaProyectos.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Esto guardará al usuario en la base de datos
            login(request, user)
            return redirect('Inicio')  # Redirige al usuario a la página de inicio después del registro exitoso
    else:
        form = UserRegistrationForm()

    return render(request, 'paginas/signUpPage.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Inicio')
            else:
                error_message = "Nombre de usuario o contraseña incorrectos."
        else:
            error_message = "Nombre de usuario o contraseña incorrectos."
    else:
        form = UserLoginForm()
        error_message = None

    return render(request, 'paginas/loginPage.html', {'form': form, 'error_message': error_message})
            