from django import forms
from django.contrib.auth.models import User
from .models import Pregunta
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
