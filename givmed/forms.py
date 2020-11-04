from django import forms
from givmed.models import User
from django.contrib.auth.forms import UserCreationForm


        
class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=60 ,required=True)
    last_name = forms.CharField(max_length=30,required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name','last_name','address','password1','password2')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')



    #       def clean(self):
    #     email = self.cleaned_data['email']
    #     password = self.cleaned_data['password']
    #     if not authenticate(email=email, password=password):
    #         raise forms.ValidationError('Invalid login')

