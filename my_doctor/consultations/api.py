from .serializers import consultationsSerializer,getAllConsultationsSerializer
from .models import consultations
from rest_framework import viewsets, permissions , mixins


class consultationsViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = consultationsSerializer
    def get_queryset(self):
        return self.request.user.consultations.all()

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class getAllConsultations(mixins.ListModelMixin, viewsets.GenericViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = getAllConsultationsSerializer

    def get_queryset(self):
        return consultations.objects.all()