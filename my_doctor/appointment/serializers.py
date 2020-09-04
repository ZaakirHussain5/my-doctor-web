from rest_framework import serializers
from .models import appointment
from doctors.serializers import doctors_infoSerializer
from accounts.serializers import UserAuthSerializer

class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'

class appointmentsListSerializer(serializers.ModelSerializer):
    doctor = doctors_infoSerializer()
    patient = UserAuthSerializer()
    class Meta:
        model = appointment
        fields = '__all__'