from rest_framework import serializers
from .models import patient_feedbacks


class patient_feedbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient_feedbacks
        fields = '__all__'