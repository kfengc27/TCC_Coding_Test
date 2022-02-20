from django.shortcuts import render
from .models import Measurement, Alert, Threshold

# Create your views here.

def setThresholds(request):
    pass 

def setAlerts(request):
    pass 

def setMeasurementScore(type,rate,record_time,Patient):
    Measurement.objects.create(type=type, score=rate, c_time=record_time, TestBy=Patient)
# get the measurement of the specific patient 
def getMeasurementTable(Patient):
    pass 

def getMeasurementResult(score):
    pass 

# send email to reminder clician
def sendEmail():
    print("Hello")
    pass 

