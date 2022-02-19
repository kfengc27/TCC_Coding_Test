from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
# from .models import patient

class SignupForm(UserCreationForm):
    email = forms.EmailField() 
    email_confirm = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField()
    
    # class Meta: 
    #     model = patient
    #     fields=('first_name','last_name', 'email','email_confirm','date_of_birth')
