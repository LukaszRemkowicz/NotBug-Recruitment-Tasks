from typing import NoReturn
from os import error

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from Users.models import User


class CustomLoginForm(forms.Form):

    email = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def clean_email(self) -> str or NoReturn:

        email = self.cleaned_data.get("email")
        password = self.data.get('password')
        if User.objects.filter(email=email).exists():
            try:
                authenticate(email=email, password=password)
            except error:
                raise forms.ValidationError("Error")
        else:
            raise forms.ValidationError("Wrong login")
        return email


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['password1', 'password2', 'email']

    def clean_email(self) -> str or NoReturn:

        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Acount with that Email already exist"
                )

        return email
