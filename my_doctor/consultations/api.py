from .serializers import consultationsSerializer,getAllConsultationsSerializer
from .models import consultations
from rest_framework import viewsets, permissions , mixins
from doctors.models import doctors_info
from patients.models import patient_info


class consultationsViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = consultationsSerializer

    def get_queryset(self):
        return consultations.objects.all()

    def perform_create(self, serializer):
        
        doctor = doctors_info.objects.get(id=self.request.data['doctor_id'])
        cons_fee = self.request.data['consultation_amt']
        share_type = doctor.commission_type
        share_val = doctor.commission_val
        if share_type == 'Pencent':
            share_val = cons_fee * (share_val/100)
        serializer.save(patient_id=self.request.user.id, comp_share=share_val)

class getAllConsultations(mixins.ListModelMixin, viewsets.GenericViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = getAllConsultationsSerializer

    def get_queryset(self):
        day = self.request.query_params.get('today', None)
        if day:
            return consultations.objects.filter(consultation_date_time=day)

        return consultations.objects.all()

class getPatientConsultations(mixins.ListModelMixin, viewsets.GenericViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = getAllConsultationsSerializer

    def get_queryset(self):
         return self.request.user.consultations.all()

class getDoctorConsultations(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = getAllConsultationsSerializer
   
    def get_queryset(self):
        return consultations.objects.filter(doctor_id__user=self.request.user)


class specific_patient_consultations(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = getAllConsultationsSerializer

    def get_queryset(self):
        pat_id = self.request.query_params.get('pat_id')
        return consultations.objects.filter(patient= patient_info.objects.get(id=pat_id).user)