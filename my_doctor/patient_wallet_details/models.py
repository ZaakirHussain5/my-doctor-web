from django.db import models

class patient_wallet_details(models.Model):
    Patient = models.CharField(max_length=25, null=True)
    balance = models.IntegerField()
    Last_modied  = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.Patient