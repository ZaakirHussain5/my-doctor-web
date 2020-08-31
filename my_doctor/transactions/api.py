from .serializers import transactionsSerializer
from .models import transactions
from rest_framework import viewsets, permissions


class transactionsViewSet(viewsets.ModelViewSet):
    queryset = transactions.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = transactionsSerializer