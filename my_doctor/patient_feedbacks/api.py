from .serializers import patient_feedbacksSerializer
from .models import patient_feedbacks
from rest_framework import viewsets, permissions


class patient_feedbacksViewSet(viewsets.ModelViewSet):
    queryset = patient_feedbacks.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_feedbacksSerializer