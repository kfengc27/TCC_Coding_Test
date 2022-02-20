from atexit import register
from shutil import unregister_unpack_format
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# from pkg_resources import Requirement

class commonInfo(models.Model):
    sex = (
        ('male','male'),
        ('female','female')
    )
    username = models.CharField(max_length=128,unique=True, default='', primary_key=True)
    first_name = models.CharField(max_length=128, default='', null=True)
    last_name = models.CharField(max_length=128, default='', null=True)
    #TODO Password should use hashlib to encrypt
    password = models.CharField(max_length=256, default='', null=True)
    email = models.EmailField(unique=True,null=True, default='')
    date_of_birth = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=32,choices=sex,default='female')
    c_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
    def __str__(self):
        return self.first_name + ' '+ self.last_name

class Clinician(commonInfo):
    departments = {
        ('1', 'Radiology Department'),
        ('2', 'Medical Record Department'),
        ('3', 'Outpatient Department'),
        ('4', 'Inpatient Service'),
        ('5', 'Other Department')
    }
    department = models.CharField(max_length=32,choices=departments,default='female')


class Patient(commonInfo):
    MyClinician = models.ForeignKey(
        Clinician,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return "My clinician is %s " % self.MyClinician.first_name








