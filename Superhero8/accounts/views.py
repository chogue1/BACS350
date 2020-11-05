from django.shortcuts import render
from django.forms import ModelForm
from manager.models import User

class RegisterForm(ModelForm):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    
# Create your views here.
