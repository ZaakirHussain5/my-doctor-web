from django.db import models


class patient_health_info(models.Model):
    user_id = models.CharField(max_length=25, null=True)
    diabities = models.BooleanField()
    blood_presure = models.BooleanField()
    eye_sight = models.CharField(max_length=32, null=True)
    phy_disabled = models.BooleanField()
    other_deficiancy = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now_add=True)
    Modified_by = models.CharField(max_length=25, null=True)
    

    def __str__(self):
        return self.created_by