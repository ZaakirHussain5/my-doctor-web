from rest_framework import serializers
from .models import doctors_info,DoctorTimings
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.defaults import bad_request


class doctors_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctors_info
        fields = '__all__'

class DoctorTimingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorTimings
        fields = '__all__'

class AvlDoctorsListSerializer(serializers.ModelSerializer):
    doctor=doctors_infoSerializer()
    class Meta:
        model = DoctorTimings
        fields = '__all__'

class DoctorRegistration(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField(max_length=15)
    commission_val=serializers.DecimalField(max_digits=10,decimal_places=2,default=2)
    commission_type=serializers.CharField(max_length=15,default='Percent')
    Registration_Number = serializers.CharField(max_length=25)
    specialist_type = serializers.CharField(max_length=25)
    rating = serializers.IntegerField(default=0)
    consultation_fee = serializers.DecimalField(max_digits=10,decimal_places=2,default=0)
    about  = serializers.CharField(max_length=500)
    profile_pic = serializers.FileField()
    mou_file = serializers.FileField()

    def create(self, validated_data):
        try:
          user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
          details = doctors_info.objects.create(user=user,
          phone_number=validated_data['phone_number'],
          commission_val=validated_data['commission_val'],
          commission_type=validated_data['commission_type'],
          consultation_fee=validated_data['consultation_fee'],
          rating=validated_data['rating'],
          Registration_Number=validated_data['Registration_Number'],
          about=validated_data['about'],
          specialist_type=validated_data['specialist_type'],
          profile_pic=validated_data['profile_pic'],
          full_name=validated_data['full_name'],
          mou_file=validated_data['mou_file'])
          details.save()
          return user
        except IntegrityError:
          raise serializers.ValidationError("User already Exists")

class UpdateProfile(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField(max_length=15)
    commission_val=serializers.DecimalField(max_digits=10,decimal_places=2,default=2)
    commission_type=serializers.CharField(max_length=15,default='Percent')
    Registration_Number = serializers.CharField(max_length=25)
    specialist_type = serializers.CharField(max_length=25)
    consultation_fee = serializers.DecimalField(max_digits=10,decimal_places=2,default=0)
    about  = serializers.CharField(max_length=500)
    profile_pic = serializers.FileField()

    def create(self, validated_data):
        try:
            user = User.objects.get(id=validated_data["loggedInuser"])
            doctor = doctors_info.objects.get(user__id=user.id)
            print(validated_data)
            user.username=validated_data['username']
            user.email=validated_data['email']
            for key,value in validated_data.items():
                if key!='pat_id':
                    setattr(doctor,key,value)
            doctor.save()
            return user
        except IntegrityError:
            raise serializers.ValidationError("User Already Exists")


