from rest_framework import viewsets, permissions,generics,mixins
from rest_framework.response import Response

from .serializers import MedicalRecordSerializer
from .models import patient_medical_records
from doctors.models import doctors_info


class PatientMedicalRecordView(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        return self.request.user.records.all()

    def perform_create(self,serializer):
        return serializer.save(patient=self.request.user)

class DoctorPrescriptionAPI(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = MedicalRecordSerializer
    def get_queryset(self):
        return patient_medical_records.objects.filter(doctor__user=self.request.user)

    def perform_create(self,serializer):
        doctor_details = doctors_info.objects.get(user=self.request.user)
        return serializer.save(is_prescription=True,doctor=doctor_details)

    def perform_destroy(self, serializer):
        serializer.delete()
        return HttpREsponse({"ok":"ok"})


class DoctorPrescriptionAPIDelete(viewsets.ModelViewSet):
    queryset = patient_medical_records.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = MedicalRecordSerializer





class PatientPrescriptionAPI(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.user.records.filter(is_prescription=True)

    def perform_create(self,serializer):
        return serializer.save(is_prescription=True,patient=self.request.user)


class getAllPrescriptions(mixins.ListModelMixin,viewsets.GenericViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = MedicalRecordSerializer
    
    def get_queryset(self):
        return patient_medical_records.objects.filter(is_prescription=True)