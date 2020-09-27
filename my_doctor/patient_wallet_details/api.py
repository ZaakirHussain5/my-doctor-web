from .serializers import patient_wallet_detailsSerializer, WalletSerializer
from .models import patient_wallet_details
from rest_framework import viewsets, permissions
from django.core.exceptions import ObjectDoesNotExist
from transactions.models import transactions

class patient_wallet_detailsViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = patient_wallet_detailsSerializer

    def get_queryset(self):
        return patient_wallet_details.objects.all()

class WalletDetailView(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = WalletSerializer

    def get_queryset(self):
        return self.request.user.Wallet.all()


