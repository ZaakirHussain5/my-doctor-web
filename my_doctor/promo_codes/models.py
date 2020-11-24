from django.db import models

class promo_code(models.Model):
    code = models.CharField(max_length=10,unique=True)
