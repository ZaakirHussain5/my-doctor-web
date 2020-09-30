from .models import online_enquiry
from rest_framework import serializers

class online_enquiry_serializer(serializers.ModelSerializer):
    class Meta:
        model = online_enquiry
        fields = '__all__'