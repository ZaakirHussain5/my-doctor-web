from django.db import models
from django.contrib.auth.models import User
from subscription_plans.models import subscription_plans
from patients.models import patient_info
import datetime

def getEndDate():
	return datetime.datetime.now()
# Create your models here.
class PatientSubscription(models.Model):
	user = models.OneToOneField(patient_info, on_delete=models.CASCADE, related_name="patientSubscription",null=True)
	sub_date = models.DateField(auto_now_add=True)
	cons_count = models.IntegerField()
	total_count = models.IntegerField(null=True,blank=True)
	plan = models.CharField(max_length=100)
	payment_id = models.CharField(max_length=100,null=True,blank=True)
	plan_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
	gst=models.DecimalField(max_digits=10,decimal_places=1,default=0.0)
	paid_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
	plan_description=models.TextField(null=True,blank=True)
	is_active = models.BooleanField(default=False)
	is_senior = models.BooleanField(default=False)
	end_date = models.DateField(default=getEndDate)

	def __str__(self):
		return self.plan