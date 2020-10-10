from rest_framework import serializers
from .models import subscription_plans
import json


class subscription_plansSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription_plans
        fields = '__all__'
	#

