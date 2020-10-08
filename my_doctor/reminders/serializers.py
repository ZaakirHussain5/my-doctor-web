from rest_framework import serializers
from .models import Reminders

class RemindersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminders
        fields = '__al__'