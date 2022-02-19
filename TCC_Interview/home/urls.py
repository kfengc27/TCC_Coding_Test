from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.logoutView, name='logout'),
    path('authorized', views.authorized, name='authorized'),
]