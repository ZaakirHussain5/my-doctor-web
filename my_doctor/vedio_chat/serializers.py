from rest_framework import serializers
from .models import VedioChat

class VedioChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = VedioChat
        fields ='__all__'