from django import forms
from django.forms import TextInput, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "password1", "password2"]
        labels = {
            'first_name': 'Nome',
            'last_name': 'Cognome',
        }
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Cognome'
                }),
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'E-mail'
                }),
            'password1': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }),
            'password2': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }),
        }