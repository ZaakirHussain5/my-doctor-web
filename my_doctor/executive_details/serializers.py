from rest_framework import serializers
from .models import executive_details
from django.contrib.auth.models import User
from django.db import IntegrityError


class executive_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = executive_details
        fields = '__all__'

class ExecutiveRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    phone_number  = serializers.CharField()
    about = serializers.CharField()

    def create(self, validated_data):
        try:
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
            executive = executive_details.objects.create(user=user,phone_number=validated_data['phone_number'],about=validated_data['about'])
            executive.save()
            return user
        except IntegrityError:
            raise serializers.ValidationError("Executive already Exists")

