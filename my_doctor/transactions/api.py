from .serializers import transactionsSerializer
from .models import transactions
from rest_framework import viewsets, permissions


class transactionsViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = transactionsSerializer

    def get_queryset(self):
        return self.request.user.transaction.all()

    def perform_create(self,serializer):
        return serializer.save(user_id=self.request.user)