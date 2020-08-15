from rest_framework import serializers
from .models import patient_health_info


class patient_health_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient_health_info
        fields = '__all__'