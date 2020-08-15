from rest_framework import serializers
from .models import doctors_info
from accounts.serializers import userSerializer


class doctors_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctors_info
        fields = '__all__'

class doctors_listSerializer(serializers.ModelSerializer):
    user = userSerializer()
    class Meta:
        model = doctors_info
        fields = '__all__'