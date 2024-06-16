from django import forms
from django.forms import ModelForm
from myapp.models import *
from .models import User
from django.contrib.auth.forms import UserCreationForm

class LivroForm(forms.ModelForm):

    class Meta:

        model =  Livro
        fields = "__all__"
        labels = {
            "titulo": "nome",
            "descricao": "descrição",
            "imagem": "imagem",

        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
            'imagem': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            ),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )