from django.shortcuts import render
from django.forms import ModelForm
from accounts.models import User

class RegisterForm(ModelForm):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=35)

    class Meta:
        model = User
        fields = ["username","password","email","first_name","last_name"]
    
# Create your views here.
