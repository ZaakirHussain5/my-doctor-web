from django.db import models

class specialist_type(models.Model):
    special_type = models.CharField(max_length=25, null=True)
    icon = models.FileField(max_length=355, null=True)
    is_active = models.BooleanField()
    created_at =  models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=32, null=True)
    Last_modied = models.DateTimeField(auto_now_add=True)
    Modified_by = models.CharField(max_length=25, null=True)
    
    

    def __str__(self):
        return self.special_type
