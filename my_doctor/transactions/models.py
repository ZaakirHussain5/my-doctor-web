from django.db import models

class transactions(models.Model):
    ref_id = models.CharField(max_length=25, null=True)
    user_id = models.CharField(max_length=25, null=True)
    credit  = models.DecimalField(max_digits=10,decimal_places=2)
    debit = models.DecimalField(max_digits=10,decimal_places=2)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    trans_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.ref_id