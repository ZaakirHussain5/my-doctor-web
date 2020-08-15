from rest_framework import serializers
from .models import consultant_chat


class consultant_chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = consultant_chat
        fields = '__all__'