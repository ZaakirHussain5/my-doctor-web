from django.db import models
from django.contrib.auth.models import User


class patient_feedbacks(models.Model):
    patient = models.ForeignKey(User,related_name='feedbacks',on_delete=models.CASCADE)
    Subject = models.CharField(max_length=25, null=True)
    Feedback_Message = models.CharField(max_length=1000, null=True)
    Posted_Date = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.Patient