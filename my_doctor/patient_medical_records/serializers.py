from rest_framework import serializers

from patient_medical_records.models import patient_medical_records

class MedicalRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = patient_medical_records
        fields = '__all__'
