from .serializers import patient_feedbacksSerializer
from .models import patient_feedbacks
from rest_framework import viewsets, permissions


class patient_feedbacksViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = patient_feedbacksSerializer

    def get_queryset(self):
        return self.request.user.feedbacks.all()

    def perform_create(self,serializer):
        return serializer.save(patient=self.request.user)