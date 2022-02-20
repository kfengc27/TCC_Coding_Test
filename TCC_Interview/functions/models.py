from threading import Thread
from django.db import models
import sys

from h11 import InformationalResponse
sys.path.append("..")

import accounts.models as aModel 


# Create your models here.

class Measurement(models.Model):
    type = models.CharField(max_length=128, default='')
    score = models.FloatField()
    c_time = models.DateTimeField(auto_now_add=True)
    TestBy = models.ForeignKey(
        aModel.Patient,
        on_delete=models.CASCADE,
    )
    # set default ordering by time
    class Meta:
       ordering = ['-c_time']

class Alert(models.Model):
    Thresholds = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)
    belongPatient = models.ForeignKey(
        aModel.Patient,
        on_delete=models.CASCADE,
    )
    alterBy = models.OneToOneField(
        Measurement, 
        on_delete=models.CASCADE,
    )
    class Meta:
       ordering = ['-c_time']

class Threshold(models.Model):
    Threshold = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)
    belongPatient = models.ForeignKey(
        aModel.Patient,
        on_delete=models.CASCADE,
    )