from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import BillPaymentsSeralizers
from .models import BillPayments

class billPaymentsRecord(ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BillPaymentsSeralizers
    queryset = BillPayments.objects.all()
