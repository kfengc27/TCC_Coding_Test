from atexit import register
from email import message
import imp
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic 
from django.views.generic.edit import CreateView 
from django.contrib.auth.decorators import login_required

from functions.models import Measurement
# Create your views here.
from .forms import SignupForm
from .models import Clinician, Patient

import functions.views as fViews 

# @login_required(login_url='/clinician/login')
def registerPatient(request):
    if request.session.get('is_login',None) != True:
        return render(request, 'clinician/login.html')
    if request.method == 'POST':
        register_form = SignupForm(request.POST) 
        message = "Please enter the patient's information"
    # register patient's information into db.
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            date_of_birth = register_form.cleaned_data['date_of_birth'] 
            if password1 != password2:
                message = "Please make sure the password you entered is same!"
                return render(request, "clinician/register.html", locals())
            else:
                same_name_user = Patient.objects.filter(username = username)
                if same_name_user:
                    message = "The patient with same username already exist, please enter others"
                    return render(request, "clinician/register.html", locals())
                same_email_user = Patient.objects.filter(email = email)
                myClinicianObj = Clinician.objects.get(email = request.session['email'])
                Patient.objects.create(username =username, first_name = first_name, last_name = last_name,password = password1, sex = sex,email = email ,date_of_birth = date_of_birth, MyClinician = myClinicianObj  )
                # print(myClinicianObj.username)
                # new_patient.MyClinician = myClinicianObj  
                return render(request, "clinician/login.html", locals())
    register_form = SignupForm() 
    return render(request, "clinician/register.html", locals())

def login(request):
    if request.session.get('is_login',None):
        return render(request, 'clinician/authorized.html', { 'firstname': request.session['first_name'], 'lastname': request.session['last_name'] })
    print(request.method)
    if(request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            try:
                user = Clinician.objects.get(email =email)
                if user.password == password:
                    message = "Login Successfully"
                    print(message)
                    request.session['is_login'] = True
                    request.session['username'] = user.username 
                    request.session['username'] = user.username 
                    request.session['first_name'] = user.first_name 
                    request.session['last_name'] = user.last_name 
                    request.session['email'] = user.email 
                    print(message)
                    print(user.first_name)
                    print("The email in session is", request.session['email'] )
                    return render(request, 'clinician/authorized.html', { 'firstname': user.first_name, 'lastname': user.last_name })
                else:
                    message = 'password is not correct.'
            except:
                message = "email not exist"
                print(message)
    return render(request, 'clinician/login.html')

# @login_required(login_url='/clinician/login')
def authorized(request):
    return render(request, 'clinician/authorized.html', {})

def getMyPatients(request):
    # TODO Get patient table 
    # context= {'title':'My Patients Table','list':1}
    myemail = request.session['email']
    print("Start my patient pag")
    user = Clinician.objects.get(email = myemail)
    myPatients = Patient.objects.filter(MyClinician = user)
    PatientObjs = []
    for patient in myPatients:
        username = patient.username
        first_name = patient.first_name 
        last_name = patient.last_name 
        email = patient.email
        print(email)
        data_of_birth = patient.date_of_birth 
        try:
            measurementObjSets = Measurement.objects.filter(TestBy=patient)
            heart_rate = measurementObjSets[0].score 
            measurement_time = measurementObjSets[0].c_time
        except:
            heart_rate = 'N/A' 
            measurement_time = 'N/A'
        patientObj = {'username':username, 'first_name':first_name, 'last_name':last_name,'email':email,'date_of_birth':data_of_birth,'heart_rate':heart_rate,'measurement_time':measurement_time}
        PatientObjs.append(patientObj)
    return render(request, 'clinician/showmypatient.html', {'firstname': request.session['first_name'], 'patientObjs':PatientObjs})

def getPatientDashboard(request, username):
    try:
        patient = Patient.objects.get(username=username)
        username = patient.username
        request.session['patient_username'] = username 
        first_name = patient.first_name 
        last_name = patient.last_name 
        email = patient.email
        data_of_birth = patient.date_of_birth 
        measureObjs = []
        try:
            measurementObjSets = Measurement.objects.filter(TestBy=patient)
            for measure in measurementObjSets:
                heart_rate = measure.score 
                measurement_time = measure.c_time
                measureObj = {'heart_rate':heart_rate,'measurement_time':measurement_time}
                measureObjs.append(measureObj)
        except:
            heart_rate = 'N/A' 
            measurement_time = 'N/A'
            measureObj = {'heart_rate':heart_rate,'measurement_time':measurement_time}
            measureObjs.append(measureObj)   
    except:
        patient = ''
        measureObjs = []
        heart_rate = 'N/A' 
        measurement_time = 'N/A'
        measureObj = {'heart_rate':heart_rate,'measurement_time':measurement_time}
        measureObjs.append(measureObj)
    thresholdObjs = fViews.getThresholds(patient) # get all thresholds belong to the patient. 
    return render(request, 'clinician/patientdashboard.html',{'firstname': request.session['first_name'], 'patient':patient,'measureObjs':measureObjs, 'thresholdObjs':thresholdObjs})

def loginAsPatient(request):
    if request.session.get('is_login',None):
        return render(request, 'patient/patienthome.html', { 'firstname': request.session['first_name'], 'lastname': request.session['last_name'] })
    if(request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            try:
                user = Patient.objects.get(email=email)
                print(email)
                print(password)
                if user.password == password:
                    message = "Login Successfully"
                    request.session['is_login'] = True
                    request.session['username'] = user.username 
                    request.session['first_name'] = user.first_name 
                    request.session['last_name'] = user.last_name 
                    request.session['email'] = user.email 
                    return render(request, 'patient/patienthome.html', { 'firstname': user.first_name, 'lastname': user.last_name })
                else:
                    message = 'password is not correct.'
            except:
                message = "email not exist"
                print(message)
    return render(request, 'patient/patientlogin.html')

def logout(request):
    request.session.flush()
    return render(request, 'clinician/login.html')

def patientHome(request):
    return render(request, 'patient/patienthome.html', {})

def patientAddHeartRate(request):
    if request.method == 'POST':
        heartrate = request.POST.get('heartrate')
        record_time = request.POST.get('measure-time') 
        patient = Patient.objects.get(email = request.session['email'])
        type = 'Heart Rate'
        fViews.setMeasurementScore(type, heartrate, record_time,patient)
        
        fViews.detectAbnormal(type,heartrate,record_time,Patient)
        return render(request, 'patient/patientCompleteMeasurement.html', {'firstname': request.session['first_name']})
    return render(request, 'patient/patientAddHeartRate.html', {'firstname': request.session['first_name']})

def patientCompleteMeasurement(request):
    return render(request, 'patient/patientCompleteMeasurement.html', {'firstname': request.session['first_name']})

def patientShowAllMyHistory(request):
    patient = Patient.objects.get(email=request.session['email'])
    measurementObjs = Measurement.objects.filter(TestBy=patient)
    return render(request, 'patient/patientShowAllMyHistory.html', {'first_name': patient.first_name, 'last_name':patient.last_name, 'email':patient.email, 'date_of_birth': patient.date_of_birth, 'patientMeasurementObjs':measurementObjs })

def patientLogout(request):
    request.session.flush()
    return render(request, 'patient/patientlogin.html')

def setThreadholdPage(request):
    patient = Patient.objects.get(username=request.session['patient_username'])
    if request.method == 'POST':
        maxThreadhold = request.POST.get('maxthreadhold')
        minThreadhold = request.POST.get('minthreadhold')
        measurementType = request.POST.get('measurementType')
        fViews.setThresholds(maxThreadhold,minThreadhold,measurementType,patient)
        return render(request, 'clinician/setThreadholdCompletePage.html', {'firstname':request.session['first_name'],'patient':patient})
    return render(request, 'clinician/setThreadhold.html', {'firstname': request.session['first_name'], 'patient':patient})

def setThreadholdCompletePage(request):
    return render(request, 'clinician/setThreadholdCompletePage.html')





