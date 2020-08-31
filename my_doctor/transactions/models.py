from django.db import models

class transactions(models.Model):
    ref_id = models.CharField(max_length=25, null=True)
    user_id = models.CharField(max_length=25, null=True)
    credit  = models.IntegerField()
    debit = models.IntegerField()
    balance = models.IntegerField()
    trans_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.ref_id