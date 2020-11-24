from django.db import models
from django.contrib.auth.models import User
from subscription_plans.models import subscription_plans
from patients.models import patient_info

# Create your models here.
class PatientSubscription(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patientSubscription")
	patient = models.ForeignKey(patient_info, on_delete=models.CASCADE, null=True, blank=True)
	start_date = models.DateField(auto_now=True)
	end_date = models.DateField(null=True)
	plan = models.ForeignKey(subscription_plans, on_delete=models.CASCADE, null=True, blank=True)
	is_active = models.BooleanField(default=False)