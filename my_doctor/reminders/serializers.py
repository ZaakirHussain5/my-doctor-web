from rest_framework import serializers
from .models import Reminders

class RemindersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminders
        fields = ['reminder_date', 'title', 'reminder_message', 'created_at']