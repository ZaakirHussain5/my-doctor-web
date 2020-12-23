from django.db import models
from django.contrib.auth.models import User
from subscription_plans.models import subscription_plans
from patients.models import patient_info

# Create your models here.
class PatientSubscription(models.Model):
	user = models.OneToOneField(patient_info, on_delete=models.CASCADE, related_name="patientSubscription")
	sub_date = models.DateField(auto_now_add=True)
	cons_count = models.IntegerField()
	plan = models.CharField(max_length=100)
	plan_description=models.TextField(null=True,blank=True)
	is_active = models.BooleanField(default=False)