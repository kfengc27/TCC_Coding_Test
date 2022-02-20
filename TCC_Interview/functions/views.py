from django.shortcuts import render
from .models import Measurement, Alert, Threshold
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def setThresholds(maxThreadhold,minThreadhold,measurementType,patient):
    Threshold.objects.create(ThresholdScoreMax=maxThreadhold,ThresholdScoreMin = minThreadhold,type = measurementType, belongPatient = patient)

def getThresholds(patient):
    print("try to fetch the threshold objects")
    print(len(Threshold.objects.filter(belongPatient=patient)))
    return Threshold.objects.filter(belongPatient=patient)

# create Alert Object 
def setAlerts(Thresholds, c_time, Patient,Measurement):
    print("Creating alert obj.")
    print(Thresholds)
    print(c_time)
    print(Patient.first_name)
    print(Patient.last_name)
    # Measurement.alerted = True 
    print("Change the alerted variable in measurement.")
    Alert.objects.create(Thresholds=Thresholds, c_time=c_time,belongPatient=Patient,alterBy=Measurement)
    print("Create Alert Done")

def setMeasurementScore(type,rate,record_time,Patient):
    measurementObj = Measurement.objects.create(type=type, score=rate, c_time=record_time, TestBy=Patient)
    return measurementObj


#TODO Add Email 
def detectAbnormal(type,rate,record_time,Patient, thresholdObjs, Measurement): # Problem detected. 
    print("Start to detect")
    print("The no. of thredholdObjs inside detectAbnormal is", len(thresholdObjs))
    len_of_thresholdObjs = len(thresholdObjs)
    try:
        thresholdObj = thresholdObjs[len_of_thresholdObjs-1]
        if float(rate) > thresholdObj.ThresholdScoreMax:
            subject = "Alert! Abnormal measurements detected"
            message = "%s %s %s's heart rate is too high. Please go to the website to review"%(record_time, Patient.first_name, Patient.last_name)
            email_to = ['chengbin.feng@outlook.com','chengbin.feng@unsw.edu.au']
            sendEmail(subject,message,email_to)
            setAlerts(rate, record_time, Patient,Measurement)
        if float(rate) < thresholdObj.ThresholdScoreMin:
            subject = "Alert! Abnormal measurements detected"
            message = "%s %s %s's heart rate is too low. Please go to the website to review"%(record_time, Patient.first_name, Patient.last_name)
            email_to = ['chengbin.feng@outlook.com','chengbin.feng@unsw.edu.au']
            sendEmail(subject,message,email_to)
            setAlerts(rate, record_time, Patient,Measurement)
    except: 
        pass 
# get the measurement of the specific patient 

def getMeasurementTable(Patient):
    pass 

def getMeasurementResult(score):
    pass 

# send email to reminder 
def sendEmail(subject,message,email_to):
    subject = subject
    message = message
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, email_to)

def getAlert(measureObj):
    try:
        alertObjs = Alert.objects.filter(alterBy = measureObj)  #Bug is here due to a wrong function. 
        if(len(alertObjs)>0):
            return True 
    except:
        return False 