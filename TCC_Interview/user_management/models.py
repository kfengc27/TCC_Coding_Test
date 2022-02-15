from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    clinicians = models.BooleanField(default=False) # a clinicians 
    patients = models.BooleanField(default=False) # a patients 
    admin = models.BooleanField(default=False) # a superuser

    @property
    def is_patients(self):
        "Is the user a patients"
        return self.patients

    @property
    def is_clinicians(self):
        "Is the user a member of staff"
        return self.clinicians 

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
