from .serializers import consultationsSerializer,getAllConsultationsSerializer
from .models import consultations
from rest_framework import viewsets, permissions , mixins
from doctors.models import doctors_info
from patients.models import patient_info
from appointment.models import appointment as appointmentTable
from django.db.models import Sum


class consultationsViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = consultationsSerializer

    def get_queryset(self):
        return consultations.objects.all()

    def perform_create(self, serializer):
        
        doctor = doctors_info.objects.get(id=self.request.data['doctor_id'])
        appointment = appointmentTable.objects.get(id=self.request.data['appoinment_id'])
        appointment.consultation_status="Completed"
        cons_fee = appointment.paid_amount
        appointment.save()
        share_type = doctor.commission_type
        share_val = doctor.commission_val
        if share_type == 'Pencent':
            share_val = cons_fee * (share_val/100)
        
        serializer.save(patient=self.request.user, doctor_id=doctor, comp_share=share_val, consultation_amt=appointment.paid_amount)

    def perform_update(self, serializer):
        serializer.save()
        # print(serializer.doctor_consulataions)
        doctor = consultations.objects.get(id=self.request.data['consultation']).doctor_id
        consultation = consultations.objects.filter(doctor_id=doctor)
        total_rating = consultation.aggregate(Sum('consultation_rating'))
        doctor.rating = float(total_rating['consultation_rating__sum'] / consultation.count()) 
        doctor.save()
        return 




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