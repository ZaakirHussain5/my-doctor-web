from rest_framework import serializers
from patient_medical_records.models import patient_medical_records
from doctors.serializers import doctors_infoSerializer

class MedicalRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = patient_medical_records
        fields = ('id', 'patient_name', 'patient', 'record_type', 'description', 'record_files', 'is_prescription', 'doctor', 'consultation_id','Last_modied')

class MedicalRecordListSerializer(serializers.ModelSerializer):
    doctor = doctors_infoSerializer()
    class Meta:
        model = patient_medical_records
        fields = ('id', 'patient_name', 'patient', 'record_type', 'description', 'record_files', 'is_prescription', 'doctor', 'consultation_id','Last_modied')
