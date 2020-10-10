from django.db import models

class subscription_plans(models.Model):
    plan_name = models.CharField(max_length=25, null=True)
    plan_price = models.IntegerField()
    validity = models.IntegerField()
    benifits_list = models.CharField(max_length=1000,null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    Last_modied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plan_name