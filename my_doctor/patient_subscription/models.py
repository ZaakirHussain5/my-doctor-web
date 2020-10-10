from django.db import models
from django.contrib.auth.models import User
from subscription_plans.models import subscription_plans

# Create your models here.
class PatientSubscription(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patientSubscription")
	start_date = models.DateField(auto_now=True)
	end_date = models.DateField(null=True)
	plan = models.ForeignKey(subscription_plans, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=False)