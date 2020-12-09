from django.db import models
from django.contrib.auth.models import User
from patient_wallet_details.models import patient_wallet_details

class transactions(models.Model):
    ref_id = models.CharField(max_length=25, null=True)
    trans_type = models.CharField(max_length=25,null=True)
    trans_desc = models.CharField(max_length=100,null=True)
    user_id = models.ForeignKey(User,related_name="transaction",on_delete=models.CASCADE, null=True, blank=True)
    credit  = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True, default=0)
    debit = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True, default=0)
    balance = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True, default=0)
    trans_date = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.ref_id

  