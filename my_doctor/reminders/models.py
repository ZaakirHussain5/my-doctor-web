from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Reminders(models.Model):
    reminder_message = models.TextField()
    reminder_owner = models.ForeignKey(User,related_name="reminders", on_delete=models.CharField)
    appointment_id = models.IntegerField(default=0)
    