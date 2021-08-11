from django.db import models
from django.contrib.auth.models import User
from patients.models import patient_info
from doctors.models import doctors_info
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class VedioChat(models.Model):
    Call_from = models.ForeignKey(User, related_name="call_from", on_delete=models.CASCADE,null=True,blank=True)
    Call_for = models.ForeignKey(User, related_name="call_for", on_delete=models.CASCADE,null=True,blank=True)
    is_answered = models.BooleanField(default=False)
    appoinment_id = models.IntegerField(default=0)
    is_busy = models.BooleanField(default=False)
    consult_id=models.IntegerField(default=0)

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


class video_chat_session(models.Model):
    session_id = models.CharField(max_length=200)
    user_token = models.TextField(null=True,blank=True)
    Call_from = models.ForeignKey(User, related_name="call_from_user", on_delete=models.CASCADE,null=True,blank=True)
    Call_for = models.ForeignKey(User, related_name="call_for_user", on_delete=models.CASCADE,null=True,blank=True)
    appoinment_id = models.IntegerField(default=0)
    is_answered = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    consult_id = models.IntegerField(default=0)
    startTime = models.DateTimeField(null=True,blank=True)
    endTime = models.DateTimeField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

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


    