from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class patient_medical_records(models.Model):
    patient = models.OneToOneField(User,related_name='patient_medical',on_delete=models.CASCADE)
    record_type = models.CharField(max_length = 255, null=True, blank=True)
    description = models.CharField(max_length = 255, null=True, blank=True)
    record_files = models.FileField(upload_to ='uploads', null=True, blank=True) 
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.patient)