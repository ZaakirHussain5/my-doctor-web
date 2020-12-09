from rest_framework import serializers
from .models import VedioChat,video_chat_session

class VedioChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = VedioChat
        fields = ('id','Call_from','Call_for','caller_name','caller_ID', 'appoinment_id', 'is_answered')

class video_mobile_serializer(serializers.ModelSerializer):
    class Meta:
        model = video_chat_session
        fields = ('id','Call_from','Call_for','session_id','doctor_token','patient_token','caller_name','caller_ID', 'appoinment_id', 'is_answered')