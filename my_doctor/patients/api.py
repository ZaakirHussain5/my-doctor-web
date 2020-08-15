from .serializers import patient_health_infoSerializer
from .models import patient_health_info
from rest_framework import viewsets, permissions


class patient_health_infoViewSet(viewsets.ModelViewSet):
    queryset = patient_health_info.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_health_infoSerializer