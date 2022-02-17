from typing_extensions import Required
from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from pkg_resources import Requirement

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    unqiue_number = models.CharField(max_length=36, default=uuid.uuid4, editable=False) # source: https://stackoverflow.com/questions/16925129/generate-unique-id-in-django-from-a-model-field
    date_joined = models.DateTimeField(default=timezone.now)
    # is_active = models.BooleanField(default=True)
    # clinicians = models.BooleanField(default=False) # a clinicians 
    # patients = models.BooleanField(default=False) # a patients 
    # admin = models.BooleanField(default=False) # a superuser
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


Department_Choices = (
    ('1', 'Radiology Department'),
    ('2', 'Medical Record Department'),
    ('3', 'Outpatient Department'),
    ('4', 'Inpatient Service'),
    ('5', 'Other Department')
)

class Clinician(User):
    USERNAME_FIELD = 'email'
    department = models.CharField(max_length=1, choices=Department_Choices)
    clinician_no = models.CharField(max_length=8 ) 
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']
    








