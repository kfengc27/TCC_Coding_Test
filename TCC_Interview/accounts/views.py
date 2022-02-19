from multiprocessing import context
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SignupForm
from django.views import generic 
from django.views.generic.edit import CreateView 
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url='/login')
class signupClinicianView(CreateView):
    # return render(request, 'registration/register.html', )
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('register')