from django.db import models


class patient_feedbacks(models.Model):
    Patient = models.CharField(max_length=25, null=True)
    Subject = models.CharField(max_length=25, null=True)
    Feedback_Message = models.CharField(max_length=1000, null=True)
    Posted_Date = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.Patient