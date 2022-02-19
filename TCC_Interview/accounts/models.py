from atexit import register
from typing_extensions import Required
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# from pkg_resources import Requirement

class test(models.Model):
    # id = models.CharField(default='')
    sex = (
        ('male','male'),
        ('female','female')

    )
    name = models.CharField(max_length=128,unique=True, default='')
    password = models.CharField(max_length=256, default='')
    email = models.EmailField(unique=True, default='')
    sex = models.CharField(max_length=32,choices=sex,default='female')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    
# Create your models here.
# class patient():
#     uid = models.UUIDField(
#         default=None,
#         blank=True,
#         null=True,
#         unique=True,
#     )
#     USERNAME_FIELD = "uid"
#     first_name = models.CharField(max_length=30, default='')
#     last_name = models.CharField(max_length=30, default='')
#     date_of_birth = models.DateField(default='')
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#         default=''
#     )
#     password = models.CharField(max_length=30, default='12345678')
#     date_joined = models.DateTimeField(default=timezone.now)
#     new_field = models.CharField(max_length=140, null=True)
#     # created_by = models.OneToOneField(User, default = "")
#     created_by = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True, null=True)

class Measurement():
    number = models.CharField(max_length=30)










