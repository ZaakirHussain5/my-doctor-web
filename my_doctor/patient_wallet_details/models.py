from django.db import models
from django.contrib.auth.models import User

class patient_wallet_details(models.Model):
    patient = models.ForeignKey(User,related_name="Wallet",on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True, default=0)
    Last_modied  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.patient)