from rest_framework import serializers
from .models import patient_info,medical_history,groups
from django.contrib.auth.models import User
from django.db import IntegrityError


class patient_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient_info
        fields = '__all__'

class PatientResgistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField(allow_blank=True,allow_null=True)
    pat_id = serializers.CharField()
    full_name = serializers.CharField()
    gender = serializers.CharField()
    dob = serializers.CharField(allow_blank=True,allow_null=True)
    age = serializers.IntegerField()
    blood_group = serializers.CharField(allow_blank=True,allow_null=True)
    rel_type = serializers.CharField(allow_blank=True,allow_null=True)
    relation = serializers.CharField(allow_blank=True,allow_null=True)
    ph_no=serializers.CharField()
    s_ph_no=serializers.CharField(allow_blank=True,allow_null=True)
    pref_lang = serializers.CharField(allow_blank=True,allow_null=True)
    street_address = serializers.CharField(allow_blank=True,allow_null=True)
    locality = serializers.CharField(allow_blank=True,allow_null=True)
    city = serializers.CharField(allow_blank=True,allow_null=True)
    pincode=serializers.CharField(allow_blank=True,allow_null=True)
    medical_history = serializers.CharField(allow_blank=True,allow_null=True)
    other_history=serializers.CharField(allow_blank=True,allow_null=True)
    groups=serializers.CharField(allow_blank=True,allow_null=True)
    profile_pic=serializers.FileField(allow_null=True)

    def create(self, validated_data):
        try:
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
            patient_details = patient_info.objects.create(user=user,
            pat_id=validated_data['pat_id'],
            full_name=validated_data['full_name'],
            gender=validated_data['gender'],
            dob=validated_data['dob'],
            age=validated_data['age'],
            blood_group=validated_data['blood_group'],
            rel_type=validated_data['rel_type'],
            relation=validated_data['relation'],
            ph_no=validated_data['ph_no'],
            s_ph_no=validated_data['s_ph_no'],
            pref_lang=validated_data['pref_lang'],
            street_address = validated_data['street_address'],
            locality = validated_data['locality'],
            city = validated_data['city'],
            pincode = validated_data['pincode'],
            medical_history = validated_data['medical_history'],
            other_history = validated_data['other_history'],
            groups = validated_data['groups'],
            profile_pic = validated_data['profile_pic'])
            patient_details.save()
            return user
        except IntegrityError:
            raise serializers.ValidationError("User Already Exists")

class PatientResgistrationApp(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    pat_id = serializers.CharField()
    full_name = serializers.CharField()
    gender = serializers.CharField()
    age = serializers.IntegerField()
    height=serializers.DecimalField(max_digits=10,decimal_places=2)
    weight=serializers.DecimalField(max_digits=10,decimal_places=2)
    marital_status=serializers.CharField()
    blood_group = serializers.CharField()
    ph_no=serializers.CharField()

    def create(self, validated_data):
        try:
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
            patient_details = patient_info.objects.create(user=user,
            pat_id=validated_data['pat_id'],
            full_name=validated_data['full_name'],
            gender=validated_data['gender'],
            age=validated_data['age'],
            blood_group=validated_data['blood_group'],
            ph_no=validated_data['ph_no'],
            height=validated_data['height'],
            weight=validated_data['weight'],
            marital_status=validated_data['marital_status'])
            patient_details.save()
            return user
        except IntegrityError:
            raise serializers.ValidationError("User Already Exists")



class medical_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = medical_history
        fields = '__all__'

class groupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = groups
        fields = '__all__'
