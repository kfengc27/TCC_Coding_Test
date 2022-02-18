from django.urls import path

from . import views 

urlpatterns = [
    path('home', views.home),
    path('login', views.LoginInterfaceView.as_view()),
]