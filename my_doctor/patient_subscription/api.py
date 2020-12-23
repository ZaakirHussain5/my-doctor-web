from rest_framework import viewsets, permissions
from rest_framework.response import Response
from datetime import date, timedelta
from .serializers import PatientSubscriptionSerializers
from .models import PatientSubscription
from subscription_plans.models import subscription_plans
from patients.models import patient_info

class MySubscriptionPlans(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PatientSubscriptionSerializers

    def get_queryset(self):
        user = patient_info.objects.get(user=self.request.user)
        return PatientSubscription.objects.filter(user=user, is_active=True)

    def perform_create(self, serializer):
        user = patient_info.objects.get(user=self.request.user)
        return serializer.save(user = user)
    
    def perform_update(self,serializer,validated_data):
        user = patient_info.objects.get(user=self.request.user)

class allSubscriptionForAdmin(viewsets.ModelViewSet):
    serializer_class = PatientSubscriptionSerializers
    permissions = [
        permissions.AllowAny
    ]

    queryset = PatientSubscription.objects.all()