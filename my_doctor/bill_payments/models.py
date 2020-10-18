from django.db import models

# Create your models here.

class BillPayments(models.Model):
    bill_type=models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    paid_date = models.DateField()
    bill_amount = models.IntegerField()
    paid_by = models.CharField(max_length=100)
    bill_date = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    
