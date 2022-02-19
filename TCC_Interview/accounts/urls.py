from django.urls import path

from . import views 

urlpatterns = [
    path('register',views.signupClinicianView.as_view(), name='register' )
]