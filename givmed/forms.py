from django import forms
from givmed.models import User
from django.contrib.auth.forms import UserCreationForm


        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60 ,required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name','last_name','address','password1','password2')