from .serializers import consultationsSerializer
from .models import consultations
from rest_framework import viewsets, permissions


class consultationsViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = consultationsSerializer
    def get_queryset(self):
        return self.request.user.consultations.all()

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)