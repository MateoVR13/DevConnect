from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), help_text='')

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name','password')