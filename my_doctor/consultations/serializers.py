from rest_framework import serializers
from .models import consultations
from doctors.serializers import doctors_infoSerializer
from accounts.serializers import UserAuthSerializer


class consultationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = consultations
        fields = '__all__'

class getAllConsultationsSerializer(serializers.ModelSerializer):
    doctor = doctors_infoSerializer()
    patient = UserAuthSerializer()
    
    class Meta:
        model = consultations
        fields = '__all__'