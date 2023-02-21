from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class RegistrationUserForm(UserCreationForm):
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email', 'password1', 'password2'


class UpdateUserForm(UserChangeForm):
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email'
