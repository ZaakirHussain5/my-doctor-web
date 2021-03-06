from django.db import models
from vedio_chat.models import video_chat_session

class consultant_chat(models.Model):
    session_id = models.ForeignKey(video_chat_session, on_delete=models.CASCADE, null=True, blank=True)
    user = models.CharField(max_length=30, default="")
    message = models.CharField(max_length=2500, null=True)
    message_date_time  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user