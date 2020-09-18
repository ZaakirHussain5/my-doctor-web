from django.db import models
from consultations.models import consultations

class consultant_chat(models.Model):
    consultation_id = models.ForeignKey(consultations,on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    message = models.CharField(max_length=25, null=True)
    attachment = models.BooleanField()
    attached_file  = models.CharField(max_length=25, null=True)
    message_date_time  = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.consultation_id