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


# def login(request):
#     print(request.method)
#     if(request.method == 'POST'):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         if email and password:
#             try:
#                 print("Search")
#                 print(email)
#                 print(password)
#                 print(models.Clinician.objects.get(email=email))
#                 # user = models.Clinician.objects.fileter(email = email)
#                 print(user)
#                 if user.password == password:
#                     print('correct')
#             except:
#                 message = "email not exist"
#     return render(request, 'home/login.html')


# @login_required(login_url='/login')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

def home(request):
    return render(request, 'home/welcome.html', {'today':datetime.today()})






