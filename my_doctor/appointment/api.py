from .serializers import appointmentSerializer,appointmentsListSerializer
from .models import appointment
from rest_framework import viewsets, permissions,mixins
from datetime import date, datetime


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
        return appointment.objects.filter(patient = self.request.user).exclude(consultation_status='pending')

class getUpcomingAppoinment(viewsets.ModelViewSet):
    serializer_class = appointmentsListSerializer
    permission = (
        permissions.IsAuthenticated
    )

    def get_queryset(self):
        return appointment.objects.filter(consultation_status = 'pending', patient=self.request.user)

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
        return appointment.objects.all()


