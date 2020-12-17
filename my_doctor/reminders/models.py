from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Reminders(models.Model):
    reminder_date = models.DateField(default=date.today )
    title = models.CharField(max_length = 200, default="")
    reminder_message = models.TextField()
    reminder_owner = models.ForeignKey(User,related_name="reminders", on_delete=models.CharField)
    created_at = models.DateTimeField(auto_now=True)