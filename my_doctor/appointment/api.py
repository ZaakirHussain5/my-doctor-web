from .serializers import appointmentSerializer,appointmentsListSerializer
from .models import appointment
from rest_framework import viewsets, permissions,mixins


class appointmentViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = appointmentSerializer
    def get_queryset(self):
        return self.request.user.appointments.all()

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class getPatientAppointments(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = appointmentsListSerializer
   
    def get_queryset(self):
        return self.request.user.appointments.all()


