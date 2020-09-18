from django.db import models
from doctors.models import doctors_info

class doctor_payments(models.Model):
    Doctor = models.ForeignKey(doctors_info,on_delete=models.CASCADE)
    Consultations_count = models.IntegerField()
    Total_amt  = models.IntegerField()
    Comm_amt = models.IntegerField()
    Amount_payable = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    Last_modied = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Doctor
