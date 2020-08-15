from rest_framework import serializers
from .models import specialist_type


class specialist_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = specialist_type
        fields = '__all__'