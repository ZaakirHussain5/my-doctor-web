from django.db import models

class feedback_replies(models.Model):
    Feedback = models.CharField(max_length=25, null=True)
    user = models.CharField(max_length=25, null=True)
    Reply_Message = models.CharField(max_length=1000, null=True)
    Posted_Date = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.Feedback