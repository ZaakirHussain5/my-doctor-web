from .serializers import consultationsSerializer,getAllConsultationsSerializer
from .models import consultations
from rest_framework import viewsets, permissions , mixins
from doctors.models import doctors_info
from patients.models import patient_info
from appointment.models import appointment as appointmentTable
from django.db.models import Sum
from datetime import date as dates



def getDateFormat(date_time):
    date = date_time.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    d = dates( year, month, day )
    # year = '{:02d}'.format(d.year)
    # month = '{:02d}'.format(d.month)
    # day = '{:02d}'.format(d.day)
    # formated_date = '{0}-{1}-{2}'.format(year, month, day)

    return d

def today_collected_commision():
    date = dates.today()
    print(date)
    appointments = consultations.objects.filter(consultation_date_time__date= date).aggregate(Sum('comp_share'))
    
    return appointments


def range_of_collected_comission(from_date, to_date):
    from_times = getDateFormat(from_date)
    to_times = getDateFormat(to_date)
    total_commision = consultations.objects.filter(consultation_date_time__date__range=(from_times, to_times)).aggregate(Sum('comp_share'))
    return total_commision



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
        if share_type == 'Percent':
            share_val = cons_fee * (share_val/100)
        
        serializer.save(patient=self.request.user, doctor_id=doctor, comp_share=share_val, consultation_amt=appointment.paid_amount)

    def perform_update(self, serializer):
        serializer.save(send_signals=False)
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