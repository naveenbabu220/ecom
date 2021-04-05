from django.shortcuts import render,redirect
from .models import Account
from.form import Form
from django.contrib.auth import authenticate,login

# Create your views here.
def sineup(req):
    if req.method == 'POST':
        x = Form(req.POST)
        if x.is_valid():
            x.save()
            email = x.cleaned_data.get('email')
            password = x.cleaned_data.get('password1')
            account = authenticate(email = email,password = password)
            login(req,account)
            redirect(sineup)
    else:
        x = Form()
    return render(req,'user/sineup.html',{'form':x})