from rest_framework import serializers
from .models import user_details
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from doctors.models import doctors_info
from patients.models import patient_info
from executive_details.models import executive_details
from django.core.exceptions import ObjectDoesNotExist
from doctors.models import doctors_info

class UserAuthSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = '__all__'

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    phone_no = serializers.CharField(max_length=32)
    full_name = serializers.CharField(max_length=25)
    age = serializers.IntegerField()

    def create(self, validated_data):
        try:
          user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
          details = user_details.objects.create(user=user,phone_no=validated_data['phone_no'],full_name=validated_data['full_name'],user_type=validated_data['user_type'],age=validated_data['age'])
          details.save()
          return user
        except IntegrityError:
          return serializers.ValidationError("User Already Exists")
        

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()
  user_type = serializers.CharField()

  def validate(self, data):
    print(data['username'])
    try:
      if data['user_type'] == 'D':
        ph_no = int(data['username'])
        doctor = doctors_info.objects.get(phone_number=ph_no)
        data['username'] = doctor.user.username
    except:
      pass 
    user = authenticate(**data)
    if user and user.is_active:
      try:
        user_type = data['user_type']
        if user_type == 'P':
          patDetails = patient_info.objects.get(user__id = user.id, is_active=True)
          patDetails.is_logged_in = True
          patDetails.save()
          if patDetails :
            return user
        if user_type == 'D':
          patDetails = doctors_info.objects.get(user__id = user.id, is_active=True)
          if patDetails:
            patDetails.is_loggedin = True
            patDetails.save()
            return user
        if user_type == 'E':
          patDetails = executive_details.objects.get(user__id = user.id)
          if patDetails :
            return user
        if user_type == 'A':
          if user.is_superuser:
            return user
      except ObjectDoesNotExist:
        pass

    raise serializers.ValidationError("Incorrect Credentials")


class socialSerializer(serializers.Serializer):
  # username = serializers.CharField()
  email = serializers.CharField()
  full_name = serializers.CharField()
  
  def create(self, validated_data):
    print(validated_data)
    try:
      return  User.objects.get(username = validated_data['email'])
    except User.DoesNotExist:
      user = User(username=validated_data['email'], email=validated_data['email'])
      user.save()
      details = user_details.objects.create(user=user,full_name=validated_data['full_name'],user_type=validated_data['user_type'])
      details.save()
      return user

    