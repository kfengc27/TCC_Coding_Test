from pyexpat import model
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

def home(request):
    return render(request, 'home/welcome.html', {'today':datetime.today()})

def handler404(request, *args, **argv):
    response = render('404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('500.html')
    response.status_code = 500
    return response






