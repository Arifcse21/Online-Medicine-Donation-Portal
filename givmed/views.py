from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from givmed.models import User
from django import forms
from givmed.forms import RegistrationForm, LoginForm, EditProfile
from django.contrib.auth import views as auth_views



# Create your views here.


def index(request):
    return render(request, 'givmed/index.html')



def register(request):
    title = '-register'
    if request.method == "POST":
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! Please login')
            return redirect('index')
        
    else:
        form = RegistrationForm()
    return render(request, 'givmed/registration.html',{'form': form,'title':title})

def profile(request):
    title = '-profile'
    if request.method == "POST":
        form = EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    
    else:
        form = EditProfile(instance=request.user)
        return render(request,'givmed/user_profile.html',{'title':title,'form':form})




def logout_view(request):
    logout(request)
    messages.success(request,'You have successfully logged out.')
    return redirect('index')


