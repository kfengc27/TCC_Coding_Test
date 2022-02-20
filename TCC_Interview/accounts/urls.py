from django.urls import path, include 
from django.conf.urls import url
from . import views 

urlpatterns = [
    path('register',views.registerPatient, name='register' ),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name ='logout'),
    path('authorized', views.authorized, name='authorized'),
    path(r'authorized/showpatient', views.getMyPatients,name='getpatient'),
    path('patient/login/', views.loginAsPatient, name='patientLogin'),
    path('patient/logout/', views.patientLogout, name='patientLogout'),
    path('patient/home/', views.patientHome, name='patientHome'),
    path('patient/addHeartRate/', views.patientAddHeartRate, name='patientAddHeartRate'),
    path('patient/patientCompleteMeasurement/', views.patientCompleteMeasurement, name='patientCompleteMeasurement'),
    path('patient/patientShowAllMyHistory/', views.patientShowAllMyHistory, name='patientShowAllMyHistory'),
    path(r'authorized/showpatient', views.getMyPatients,name='getpatient'),
    url(r'^captcha', include('captcha.urls'))
]