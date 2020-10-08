from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reminders(models.Model):
    reminder_date = models.DateTimeField()
    reminder_message = models.TextField()
    reminder_owner = models.ForeignKey(User,related_name="reminders", on_delete=models.CharField)
    created_at = models.DateTimeField(auto_now=True)