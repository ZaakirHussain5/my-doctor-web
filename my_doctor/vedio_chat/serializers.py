from rest_framework import serializers
from .models import VedioChat

class VedioChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = VedioChat
        fields = ('id','Call_from','Call_for','Call_session','patient_name')