from django import forms
from givmed.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


        
class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=60 ,required=True)
    last_name = forms.CharField(max_length=30,required=False)

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
            'password',
            )

