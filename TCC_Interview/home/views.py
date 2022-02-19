from re import template
from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views.generic.edit import CreateView 
# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



# @login_required(login_url='/login')
# def signupClinicianView(request):
#     form = UserCreationForm()  
#     context = {  
#         'form':form  
#     }  
#     return render(request, 'clinician/register.html', context)

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

@login_required(login_url='/login')   
def logoutView(request):
    return render(request, 'home/logout.html')

@login_required(login_url='/login')
def authorized(request):
    return render(request, 'home/authorized.html', {})

def home(request):
    return render(request, 'home/welcome.html', {'today':datetime.today()})





