from django import forms
from .models import User, Notes
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_admin', 'is_customer']

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['heading', 'text']