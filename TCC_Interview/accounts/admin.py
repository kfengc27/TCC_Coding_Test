from django.contrib import admin
from .models import Clinician
from .models import Patient

class ClinicianAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','sex', 'email','c_time','date_of_birth')
    search_fields = ['first_name','email']

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','sex', 'email','c_time','date_of_birth','MyClinician')
    search_fields = ['first_name','email']

admin.site.register(Clinician,ClinicianAdmin)
admin.site.register(Patient, PatientAdmin)