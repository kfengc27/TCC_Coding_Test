from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
# from .models import patient
from django.contrib.admin.widgets import AdminDateWidget
from captcha.fields import CaptchaField
from bootstrap_datepicker_plus.widgets import DatePickerInput

class DateInput(forms.DateInput):
    input_type = 'date'

class SignupForm(forms.Form):
    gender = (
        ('male', "Male"),
        ('female', "Female"),
    )
    username = forms.CharField(label="User Name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First Name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Sex', choices=gender)
    date_of_birth = forms.DateField(label="Date Of Birth", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    captcha = CaptchaField(label='Vertify Code')
    # class Meta: 
    #     model = patient
    #     fields=('first_name','last_name', 'email','email_confirm','date_of_birth')
