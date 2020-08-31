from .serializers import doctor_paymentsSerializer
from .models import doctor_payments
from rest_framework import viewsets, permissions


class doctor_paymentsViewSet(viewsets.ModelViewSet):
    queryset = doctor_payments.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = doctor_paymentsSerializer