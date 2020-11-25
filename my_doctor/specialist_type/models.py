from django.db import models

class specialist_type(models.Model):
    special_type = models.CharField(max_length=25)
    created_at =  models.DateTimeField(auto_now_add=True)
    Last_modied = models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.special_type
