from django import forms
from.models import Account
from django.contrib.auth.forms import UserCreationForm

class Form(UserCreationForm):
    
    class Meta:
        model = Account
        fields = ['username','email','mobile','password1','password2']

