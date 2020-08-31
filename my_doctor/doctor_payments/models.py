from django.db import models

class doctor_payments(models.Model):
    Doctor = models.CharField(max_length=25, null=True)
    Consultations_count = models.IntegerField()
    Total_amt  = models.IntegerField()
    Comm_amt = models.IntegerField()
    Amount_payable = models.IntegerField()
    created_at = models.IntegerField()
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now_add=True)
    Modified_by = models.CharField(max_length=25, null=True)
    def __str__(self):
        return self.Doctor
