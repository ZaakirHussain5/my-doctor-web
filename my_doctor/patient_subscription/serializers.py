from rest_framework import serializers
from .models import PatientSubscription
from subscription_plans.models import subscription_plans
from datetime import date, timedelta


class PatientSubscriptionSerializers(serializers.ModelSerializer):
    # end_date = serializers.DateField(required=False)
    class Meta:
        model = PatientSubscription
        fields = "__all__"
        read_only_fields = ('user', 'patient')
        depth =1

