from rest_framework import serializers
from .models import consultations


class consultationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = consultations
        fields = '__all__'