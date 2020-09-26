from .serializers import patient_wallet_detailsSerializer
from .models import patient_wallet_details
from rest_framework import viewsets, permissions
from django.core.exceptions import ObjectDoesNotExist

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
        