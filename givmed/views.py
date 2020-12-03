from django.shortcuts import render,redirect
from django.contrib.auth import (
     login,
     authenticate, 
     logout,
     update_session_auth_hash
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from givmed.models import User, Donation
from django import forms
from givmed.forms import(
    RegistrationForm,
    LoginForm,
    EditProfile, 
    DonationForm
)
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
    title='-profile'
    return render(request, 'givmed/profile.html',{'title':title})


def edit_profile(request):
    title = '-edit profile'
    if request.method == "POST":
        form = EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    
    else:
        form = EditProfile(instance=request.user)
        return render(request,'givmed/edit_profile.html',{'title':title,'form':form})






def change_password(request):
    title = '-change password'
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'Passord Updated Successfully')
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'givmed/change_password.html',{'title':title,'form':form})


def logout_view(request):
    logout(request)
    messages.success(request,'You have successfully logged out.')
    return redirect('index')



def donation(request):
    title = '-donation'
    form = DonationForm(request.POST)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        messages.success(request,'Donation form submitted.')
        return redirect('profile')
    else:
        form = DonationForm
        return render(request, 'givmed/donation.html', {'form': form,'title':title})


