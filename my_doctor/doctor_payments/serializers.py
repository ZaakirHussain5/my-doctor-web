from rest_framework import serializers
from .models import doctor_payments
from doctors.serializers import doctors_listSerializer

class doctor_paymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor_payments
        fields = '__all__'


class DoctorPaymentsListSerializer(serializers.ModelSerializer):
	doctor = doctors_listSerializer()
	class Meta:
	    model = doctor_payments
	    fields = '__all__'
