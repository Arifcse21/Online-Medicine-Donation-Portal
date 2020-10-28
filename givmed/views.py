from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from givmed.models import User
from django import forms
from givmed.forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request, 'givmed/index.html')



def register(request):
    if request.method == "POST":
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request,f'Account created for {username}!')
            user = authenticate(username = username,password=password)
            return redirect('profile')
        
    else:
        form = RegistrationForm()
    return render(request, 'givmed/registration.html',{'form': form})

def profile(request):
    return render(request,'givmed/user_profile.html')

