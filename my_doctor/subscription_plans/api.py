from .serializers import subscription_plansSerializer
from .models import subscription_plans
from rest_framework import viewsets, permissions
from rest_framework import generics
from rest_framework.response import  Response
import json

class subscription_plansViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = subscription_plansSerializer

    def get_queryset(self):
        return subscription_plans.objects.all()

    # 
    def perform_create(self,serializer):
        
        return serializer.save()
        

    