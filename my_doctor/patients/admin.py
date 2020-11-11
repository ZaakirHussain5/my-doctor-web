from django.contrib import admin
from patients.models import patient_info, PatientBillingHistory
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['user','full_name']

admin.site.register(patient_info, PatientAdmin)
admin.site.register(PatientBillingHistory)