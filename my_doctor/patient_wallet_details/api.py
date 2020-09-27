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

    # def perform_create(self,serializer):
    #     new_balance = self.request.data["balance"]
    #     try:
    #         existing = patient_wallet_details.objects.get(patient=self.request.user.id)
    #         new_balance += existing.balance 
    #     except ObjectDoesNotExist:
    #         pass
    #     serializer.save(patient_id=self.request.user,balance=new_balance)

class WalletDetailView(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = WalletSerializer

    def get_queryset(self):
        return self.request.user.Wallet.all()

    # def get(self, request, format=None):
    #     wallet = patient_wallet_details.objects.all().values_list('patient', flat=True)
    #     wallet_id = ""
    #     for user in wallet:
    #         wallet_id = user
    #     patient = transactions.objects.filter(user_id__username = wallet_id)
    #     return Response({   
    #         "wallet_details":{
    #             "id":str(wallet_id),
    #             # "balanace":wallet_balance
    #         }
    #     }) 
