from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Worker


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ('username', 'email', 'position', 'about_user', 'user_image', 'department')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = ('username', 'email', 'position', 'about_user', 'user_image','department')
