from re import template
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.contrib.auth.views import LoginView 

def home(request):
    return render(request, 'home/welcome.html', {'today':datetime.today()})

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'




