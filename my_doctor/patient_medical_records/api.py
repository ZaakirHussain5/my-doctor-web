from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response

from patient_medical_records.serializers import MedicalRecordSerializer
from patient_medical_records.models import patient_medical_records


class PatientMedicalRecordView(viewsets.ModelViewSet):
    queryset = patient_medical_records.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = MedicalRecordSerializer