from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response

from .serializers import MedicalRecordSerializer
from .models import patient_medical_records


class PatientMedicalRecordView(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        return self.request.user.records.all()

    def perform_create(self,serializer):
        return serializer.save(patient=self.request.user)