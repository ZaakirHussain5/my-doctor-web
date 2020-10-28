from django.db import models
from django.contrib.auth.models import User
from patients.models import patient_info

# Create your models here.
class VedioChat(models.Model):
    Call_from = models.ForeignKey(User, related_name="call_from", on_delete=models.CASCADE,null=True,blank=True)
    Call_for = models.ForeignKey(User, related_name="call_for", on_delete=models.CASCADE,null=True,blank=True)
    Call_session = models.CharField(max_length=500,null=True,blank=True)

    @property
    def patient_name(self):
        return patient_info.objects.get(user__id=self.Call_from.id).full_name
    

    

    