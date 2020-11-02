from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from givmed.models import User
from django import forms
from givmed.forms import RegistrationForm, LoginForm

# Create your views here.

def index(request):
    return render(request, 'givmed/index.html')



def register(request):
    if request.method == "POST":
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request,f'Account created for {username}!')
            user = authenticate( username=username, password=password)
            return redirect('profile')
        
    else:
        form = RegistrationForm()
    return render(request, 'givmed/registration.html',{'form': form})

def profile(request):
    return render(request,'givmed/user_profile.html')

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)

            return redirect('profile')
    else:
        lform = LoginForm() 


    return render(request,'givmed/login.html',{"lform":lform})
