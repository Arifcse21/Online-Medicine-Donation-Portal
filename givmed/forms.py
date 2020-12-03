from django import forms
from givmed.models import User,Donation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from datetime import datetime


        
class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=60 ,required=True)
    last_name = forms.CharField(max_length=30,required=False)
    # propic = forms.ImageField(required= False)
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name','last_name','address', 'phone', 'password1','password2')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')



class EditProfile(UserChangeForm):


    class Meta:
        model=User
        fields = (
            'email', 
            'first_name',
            'last_name',
            'address',
            'phone',
            'profile_pic',
            'password',
            )


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields =( 
            'Medicines_Name',
            'Quantity',
            'Home_Address',
            'ZIP',
        )   