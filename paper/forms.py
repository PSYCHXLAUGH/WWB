from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *
from pdb import set_trace
from pprint import pprint


class AddPostForm(forms.ModelForm):  # come up with the name of the form yourself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Выбрать категорию'

    class Meta:
        model = Paper
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'slug': forms.TextInput(attrs={'class': "form-control"}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'cat': forms.Select(attrs={'class': 'form-select'})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-control"}))
