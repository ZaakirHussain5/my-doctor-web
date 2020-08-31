from .serializers import patient_wallet_detailsSerializer
from .models import patient_wallet_details
from rest_framework import viewsets, permissions


class patient_wallet_detailsViewSet(viewsets.ModelViewSet):
    queryset = patient_wallet_details.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_wallet_detailsSerializer