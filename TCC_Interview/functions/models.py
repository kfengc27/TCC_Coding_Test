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
    Thresholds = models.FloatField()
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
    ThresholdScoreMax = models.FloatField(default=140.00)
    ThresholdScoreMin = models.FloatField(default=70.00)
    type = models.CharField(max_length=128, default='')
    c_time = models.DateTimeField(auto_now_add=True)
    belongPatient = models.ForeignKey(
        aModel.Patient,
        on_delete=models.CASCADE,
    )
    ordering = ['-c_time']
