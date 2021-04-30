from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from main.models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    mobile = forms.IntegerField()
    city = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile', 'city', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class BioForm(ModelForm):
    class Meta:
        model = ProfileForm
        fields = "__all__"


class AluForm(ModelForm):
    class Meta:
        model = AlumniForm
        fields = "__all__"


class RegForm(ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
