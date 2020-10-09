from django.db import models

class online_enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    ph_no=models.CharField(max_length=13)
    gender=models.CharField(max_length=10)
    blood_group=models.CharField(max_length=10)
    speciality =models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    message=models.CharField(max_length=300)
    is_contacted = models.BooleanField(default=False)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name
