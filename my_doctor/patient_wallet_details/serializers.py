from rest_framework import serializers
from .models import patient_wallet_details


class patient_wallet_detailsSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data.get('patient'):
            if(self.instance):
                if patient_wallet_details.objects.filter(patient=data.get('patient')).exclude(id=self.instance.id).exists():
                    raise serializers.ValidationError({'patient': 'Patient already exists'})
            elif patient_wallet_details.objects.filter(patient=data.get('patient')).exists():
                raise serializers.ValidationError({'patient': 'Patient already exists'})
        return data

    class Meta:
        model = patient_wallet_details
        fields = '__all__'