from django import forms
from django.contrib.auth.models import User
from .models import Pregunta, Respuesta, Proyecto
from django.contrib.auth.forms import UserCreationForm

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['question_title', 'question_topic', 'question_language', 'question_body']
        

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['answer_body']
        
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['preview_image', 'project_title', 'project_language', 'project_topic', 'project_description', 'archivo_content']
