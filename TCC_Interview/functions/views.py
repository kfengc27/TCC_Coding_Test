from django.shortcuts import render
from .models import Measurement, Alert, Threshold
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def setThresholds(maxThreadhold,minThreadhold,measurementType,patient):
    Threshold.objects.create(ThresholdScoreMax=maxThreadhold,ThresholdScoreMin = minThreadhold,type = measurementType, belongPatient = patient)

def getThresholds(patient):
    return Threshold.objects.filter(belongPatient=patient)

def setAlerts(Thresholds, c_time, Patient,Measurement):
    Alert.objects.create(Thresholds=Thresholds, c_time=c_time,Patient=Patient,Measurement=Measurement)

def setMeasurementScore(type,rate,record_time,Patient):
    Measurement.objects.create(type=type, score=rate, c_time=record_time, TestBy=Patient)

#TODO Add Email 
def detectAbnormal(type,rate,record_time,Patient):
    thresholdObjs = getThresholds(Patient)
    len_of_thresholdObjs = len(thresholdObjs)
    thresholdObj = thresholdObjs[len_of_thresholdObjs-1]
    if float(rate) > thresholdObj.ThresholdScoreMax:
        subject = "Alert! Abnormal measurements detected"
        message = "%s %s %s's heart rate is too high. Please go to the website to review"%(record_time, Patient.first_name, Patient.last_name)
        email_to = ['chengbin.feng@outlook.com','chengbin.feng@unsw.edu.au', clinician_email]
        sendEmail(subject,message,email_to)
        print("email send")
    if float(rate) < thresholdObj.ThresholdScoreMin:
        subject = "Alert! Abnormal measurements detected"
        message = "%s %s %s's heart rate is too low. Please go to the website to review"%(record_time, Patient.first_name, Patient.last_name)
        email_to = ['chengbin.feng@outlook.com','chengbin.feng@unsw.edu.au',clinician_email]
        sendEmail(subject,message,email_to)
        print("eamil send")
        setAlerts(rate, record_time, Patient,Measurement)
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
