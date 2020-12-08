from .serializers import appointmentSerializer,appointmentsListSerializer, cancleAppointmentSerializer
from .models import appointment
from rest_framework import viewsets, permissions,mixins
from datetime import date, datetime
from django.db.models import Sum
from transactions.models import transactions
from patients.models import patient_info

def today_total_appointment():
    date = getDateFormat()
    print(date)
    appointments = appointment.objects.filter(appointment_date= date)
    total_fees_collected = appointments.aggregate(Sum('paid_amount'))
    obj = {
        'total_count': appointments.count(),
        'total_fees': total_fees_collected
    }
    return obj


def get_a_range_appointment(from_date, to_date):
    total_appointmetns = appointment.objects.filter(appointment_date__range=(from_date, to_date))
    total_fees_collected = total_appointmetns.aggregate(Sum('paid_amount'))
    obj = {
        'total_count': total_appointmetns.count(),
        'total_fees': total_fees_collected
    }
    return obj 

def getDateFormat():
    d = date.today()
    year = '{:02d}'.format(d.year)
    month = '{:02d}'.format(d.month)
    day = '{:02d}'.format(d.day)
    formated_date = '{0}/{1}/{2}'.format(day, month, year)

    return formated_date

class appointmentViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = appointmentSerializer

    
    def get_queryset(self):
        return self.request.user.appointments.all()

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

    def perform_update(delf, serializer):
        if serializer.is_valid(raise_exception=False):
            serializer.save()
        return 



class NewAppointmentAPI(viewsets.ModelViewSet):
    queryset = appointment.objects.all()
    serializer_class = appointmentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class getPatientAppointments(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = appointmentsListSerializer
   
    def get_queryset(self):
        return self.request.user.appointments.all()

class getAppoinmentHistory(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )
    def get_queryset(self):
        return appointment.objects.filter(patient = self.request.user).exclude(consultation_status='Pending')

class getUpcomingAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        return appointment.objects.filter(consultation_status = 'Pending', patient=self.request.user)


class upComingAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        dates = getDateFormat()
        return appointment.objects.filter(consultation_status = 'Pending', doctor=self.request.user.Doctors).exclude(appointment_date__contains=dates)


class previousAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        return appointment.objects.filter(consultation_status = 'Completed', doctor=self.request.user.Doctors)


class todaysAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        formated_date = getDateFormat()
        print(formated_date)
        return appointment.objects.filter(consultation_status = 'Pending', appointment_date__contains=formated_date,  doctor=self.request.user.Doctors)



class getDoctorAppointments(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = appointmentsListSerializer
   
    def get_queryset(self):
        return appointment.objects.filter(doctor__user=self.request.user)



class getAllAppointments(mixins.ListModelMixin, viewsets.GenericViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = appointmentsListSerializer

    def get_queryset(self):
        queryset = appointment.objects.all()
        status = self.request.query_params.get('status',None)
        now = self.request.query_params.get('now',None)
        formated_date = getDateFormat()
        print(status)
        if status is not None:
            if status == 'Completed':
                queryset =  appointment.objects.filter(consultation_status__icontains=status)
            else:
                queryset =  appointment.objects.filter(consultation_status__icontains=status).exclude(appointment_date=formated_date)
        if now is not None:
            queryset =  appointment.objects.filter(consultation_status=status,appointment_date=formated_date)
        return queryset



class cancleAppointment(viewsets.ModelViewSet):
    serializer_class = cancleAppointmentSerializer
    queryset = appointment.objects.all()
    permissions = {
        permissions.IsAuthenticated
    }
    def perform_update(self, serializer):
        appointments = serializer.save()
        if appointment.consultation_status == 'Cancle':
            now = datetime.now()
            desc = "appointment camcled on {0}".format(now.strftime("%m/%d/%Y"))
            transactions.objects.create(trans_type="appointment cancle", trans_desc=desc,user_id = self.request.user, credit=appointments.paid_amount )

        return 


class getAllAppointmentsSpecificUser(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer

    permissions = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        pat_id = self.request.query_params.get('pat_id')
        return appointment.objects.filter(patient=patient_info.objects.get(id=pat_id).user)
        
