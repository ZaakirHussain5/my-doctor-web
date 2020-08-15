from .serializers import subscription_plansSerializer
from .models import subscription_plans
from rest_framework import viewsets, permissions


class subscription_plansViewSet(viewsets.ModelViewSet):
    queryset = subscription_plans.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = subscription_plansSerializer