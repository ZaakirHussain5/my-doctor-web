from .serializers import appointmentSerializer,appointmentsListSerializer
from .models import appointment
from rest_framework import viewsets, permissions,mixins
from datetime import date, datetime


def getDateFormat():
    d = date.today()
    year = '{:02d}'.format(d.year)
    month = '{:02d}'.format(d.month)
    day = '{:02d}'.format(d.day)
    formated_date = '{0}-{1}-{2}'.format(year, month, day)

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
        return appointment.objects.filter(consultation_status = 'Pending', doctor=self.request.user.Doctors).exclude(appointment_date=dates)


class previousAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        return appointment.objects.filter(consultation_status = 'success', doctor=self.request.user.Doctors)


class todaysAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        formated_date = getDateFormat()
        return appointment.objects.filter(consultation_status = 'Pending', appointment_date=formated_date,  doctor=self.request.user.Doctors)



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
        if status is not None:
            queryset =  appointment.objects.filter(consultation_status=status).exclude(appointment_date=formated_date)
        if now is not None:
            queryset =  appointment.objects.filter(consultation_status=status,appointment_date=formated_date)
        return queryset


