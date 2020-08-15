from django.db import models
from django.contrib.auth.models import User

class consultant_chat(models.Model):
    consultation_id = models.CharField(max_length=25, null=True)
    user = models.ForeignKey(User,related_name='cons_chats',on_delete=models.SET_NULL,null=True)
    message = models.CharField(max_length=25, null=True)
    attachment = models.BooleanField()
    attached_file  = models.CharField(max_length=25, null=True)
    message_date_time  = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField()
    delivered = models.BooleanField()

    def __str__(self):
        return self.consultation_id