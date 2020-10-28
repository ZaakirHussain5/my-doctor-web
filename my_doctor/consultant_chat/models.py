from django.db import models
from consultations.models import consultations

class consultant_chat(models.Model):
    consultation_id = models.ForeignKey(consultations, on_delete=models.CASCADE, null=True, blank=True)
    user = models.CharField(max_length=30, default="")
    message = models.CharField(max_length=2500, null=True)
    message_date_time  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user