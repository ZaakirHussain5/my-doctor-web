from rest_framework import serializers
from .models import patient_wallet_details


class patient_wallet_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient_wallet_details
        fields = '__all__'