from django.db import models
from accounts.models import user_details

class doctors_info(models.Model):
    user = models.ForeignKey(user_details,related_name='Doctors',on_delete=models.CASCADE)
    Registration_Number = models.CharField(max_length=25, null=True)
    specialist_type = models.CharField(max_length=25, null=True)
    rating = models.IntegerField()
    first_consultation_fee = models.IntegerField()
    followup_consultation_fee = models.IntegerField()
    about  = models.CharField(max_length=25, null=True)
    is_acrive = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now_add=True)
    Modified_by = models.CharField(max_length=25, null=True)
    

    def __str__(self):
        return self.Registration_Number 