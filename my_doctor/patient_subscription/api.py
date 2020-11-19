from rest_framework import viewsets, permissions
from rest_framework.response import Response
from datetime import date, timedelta
from .serializers import PatientSubscriptionSerializers
from .models import PatientSubscription
from subscription_plans.models import subscription_plans

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
        subs_plan_end_date = date.today() + timedelta(days=subs_plan.validity)
        return serializer.save(end_date = subs_plan_end_date, user = self.request.user)