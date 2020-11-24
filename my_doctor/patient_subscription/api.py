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
        print(self.request.user)
        return PatientSubscription.objects.filter(user=self.request.user, is_active=True)

    def perform_create(self, serializer):
        subs_plan = subscription_plans.objects.get(id=self.request.data.get('plan'))
        print(subs_plan)
        subs_plan_end_date = date.today() + timedelta(days=subs_plan.validity)
        print(subs_plan_end_date)
        patient = patient_info.objects.get(user = self.request.user)
        print(patient)
        return serializer.save(end_date = subs_plan_end_date,plan=subs_plan, user = self.request.user, patient=patient)

    

class allSubscriptionForAdmin(viewsets.ModelViewSet):
    serializer_class = PatientSubscriptionSerializers
    permissions = [
        permissions.AllowAny
    ]

    queryset = PatientSubscription.objects.all()