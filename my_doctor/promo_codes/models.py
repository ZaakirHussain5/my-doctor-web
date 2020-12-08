from django.db import models

class promo_code(models.Model):
    code = models.CharField(max_length=10,unique=True)
    discount_percent = models.DecimalField(max_digits=10,decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)

