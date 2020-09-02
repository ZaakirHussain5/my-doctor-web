from django.db import models
from django.contrib.auth.models import User

class executive_details(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=32,null=True)
    profile_pic=models.FileField(null=True)
    phone_number  = models.CharField(max_length=25, null=True)
    about = models.CharField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25, null=True)
    Last_modied = models.DateTimeField(auto_now=True)
    Modified_by = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.user.username