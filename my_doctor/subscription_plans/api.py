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

    def create(self, request):
        benifits_lists = request.data.get('benifits_list')
        benifits_lists = json.dumps(benifits_lists)
        plan_obj = subscription_plans(
            plan_name=request.data.get('plan_name'),
            plan_price=request.data.get('plan_price'),
            validity=request.data.get('validity'),
            benifits_list=benifits_lists
        )
        plan_obj.save()
        return Response({
            "plan": subscription_plansSerializer(plan_obj).data
        })
