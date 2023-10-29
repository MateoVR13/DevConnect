from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, initial="")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, initial="")
    first_name = forms.CharField(max_length=60, required=True, initial="")
    last_name = forms.CharField(max_length=60, required=True, initial="")
    email = forms.EmailField(max_length=254, required=True, initial="")

    class Meta:
        model = Usuario
        fields = ('username','password', 'email', 'first_name', 'last_name')
        
        
class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Contraseña")