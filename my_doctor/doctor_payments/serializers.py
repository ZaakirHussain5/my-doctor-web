from rest_framework import serializers
from .models import doctor_payments


class doctor_paymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor_payments
        fields = '__all__'