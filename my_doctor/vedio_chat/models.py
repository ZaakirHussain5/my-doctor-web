from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VedioChat(models.Model):
    Call_from = models.ForeignKey(User, related_name="call_from", on_delete=models.CASCADE)
    Call_for = models.ForeignKey(User, related_name="vall_for", on_delete=models.CASCADE)
    Call_Link = models.CharField(max_length=500)
    