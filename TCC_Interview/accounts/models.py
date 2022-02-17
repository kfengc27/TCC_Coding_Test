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
    created_at = models.DateTimeField(auto_now_add=True)
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

# class TCCUser(AbstractUser):
#     phr_relate = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
#     token = models.EmailField(null=True, blank=True)
#     USER_CHOICES = (
#         ('1', 'Doctor'),
#         ('2', 'Patient')
#     )
#     user_type = models.CharField(choices=USER_CHOICES, max_length=10)


# class Patient(User):
#     pass 

class Clinician(User):
    pass 



