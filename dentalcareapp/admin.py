from django.contrib import admin
from .models import Dentist, Patient, Appointment

# Register your models here.

class DentistAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class AppointmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Dentist, DentistAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
