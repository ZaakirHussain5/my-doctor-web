from rest_framework import serializers
from .models import PatientSubscription
from subscription_plans.models import subscription_plans
from datetime import date, timedelta
from patients.serializers import patient_infoSerializer


class PatientSubscriptionSerializers(serializers.ModelSerializer):
    user = patient_infoSerializer(required=False)
    class Meta:
        model = PatientSubscription
        fields = "__all__"
        read_only=('sub_date', )

