from django.db import models
from django.contrib.auth.models import User
from doctors.models import doctors_info

# Create your models here.

class patient_medical_records(models.Model):
    patient = models.ForeignKey(User,related_name='records',on_delete=models.CASCADE,null=True)
    record_type = models.CharField(max_length = 255, null=True, blank=True)
    description = models.CharField(max_length = 255, null=True, blank=True)
    record_files = models.FileField(upload_to ='uploads', null=True, blank=True) 
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now=True)
    is_prescription =models.BooleanField(default=False)
    doctor = models.ForeignKey(doctors_info,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.patient)