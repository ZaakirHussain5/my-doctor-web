from .serializers import doctor_paymentsSerializer, DoctorPaymentsListSerializer
from .models import doctor_payments
from rest_framework import viewsets, permissions
from doctors.models import doctors_info

class doctor_paymentsViewSet(viewsets.ModelViewSet):
    queryset = doctor_payments.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = doctor_paymentsSerializer


class doctor_listViewset(viewsets.ModelViewSet):
    queryset = doctor_payments.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DoctorPaymentsListSerializer

