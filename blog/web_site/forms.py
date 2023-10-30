from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'short_description', 'full_description', 'photo', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статьи'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите краткое описание статьи'
            }),
            'full_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полное описание статьи'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(min_length=8, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Введите ваш username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Введите ваш password"
    }))

    class Meta:
        model = User


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Введите ваш password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Введите ваш password ещё раз"
    }))

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите ваш username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email"
            })
        }