from django.db import models
from doctors.models import doctors_info

class doctor_payments(models.Model):
    doctor = models.OneToOneField(doctors_info,on_delete=models.CASCADE,null=True, blank=True)
    consultations_count = models.IntegerField(null=True, blank=True) #increment 
    total_amt  = models.IntegerField(null=True, blank=True, default=0) #consultation_amt 
    comm_amt = models.IntegerField(null=True, blank=True, default=0) #comp_share
    amount_payable = models.IntegerField(null=True, blank=True, default=0) #total_amt - comm_amt
    created_at = models.DateTimeField(auto_now_add=True)
    last_modied = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.doctor)
