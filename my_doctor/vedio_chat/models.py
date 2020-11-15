from django.db import models
from django.contrib.auth.models import User
from patients.models import patient_info
from doctors.models import doctors_info
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class VedioChat(models.Model):
    Call_from = models.ForeignKey(User, related_name="call_from", on_delete=models.CASCADE,null=True,blank=True)
    Call_for = models.ForeignKey(User, related_name="call_for", on_delete=models.CASCADE,null=True,blank=True)

    @property
    def caller_name(self):
        try:
            return patient_info.objects.get(user__id=self.Call_from.id).full_name
        except ObjectDoesNotExist:
            return doctors_info.objects.get(user__id=self.Call_from.id).full_name
    
    @property
    def caller_ID(self):
        try:
            return patient_info.objects.get(user__id=self.Call_from.id).id
        except ObjectDoesNotExist:
            return doctors_info.objects.get(user__id=self.Call_from.id).id
    
    