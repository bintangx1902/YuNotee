from django import forms as f
from .models import *
from django.contrib.auth.forms import UserCreationForm, User


class NoteModelForm(f.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note', 'file']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
