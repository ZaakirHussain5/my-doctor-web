from rest_framework import viewsets, permissions
from rest_framework.response import Response
from datetime import date, timedelta
from .serializers import PatientSubscriptionSerializers
from .models import PatientSubscription
from subscription_plans.models import subscription_plans
from patients.models import patient_info,PatientBillingHistory


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
        PatientBillingHistory.objects.create(patient=user,doc_name=self.request.data['plan'] + " Plan",
        doc_spl="Subscrition Plan Activated",amount=self.request.data['paid_amount'],
        description="Amount Deducted for Subscription",
        doc_image='2.png',status="P")
        return serializer.save(user = user,total_count=self.request.data['cons_count'])
        

class allSubscriptionForAdmin(viewsets.ModelViewSet):
    serializer_class = PatientSubscriptionSerializers
    permissions = [
        permissions.AllowAny
    ]

    queryset = PatientSubscription.objects.all()