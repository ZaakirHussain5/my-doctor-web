from django.db import models
from django.contrib.auth.models import User

class user_details(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=32)
    full_name = models.CharField(max_length=25)
    user_type = models.CharField(max_length=32)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    weight = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    profile_pic = models.FileField(max_length=355, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=25, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.full_name+ ',' +self.user_type