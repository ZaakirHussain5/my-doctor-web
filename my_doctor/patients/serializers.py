from rest_framework import serializers
from .models import patient_info,medical_history,groups
from django.contrib.auth.models import User
from django.db import IntegrityError


class patient_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient_info
        fields = '__all__'
        depth= 1

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


class UpdateProfile(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    full_name = serializers.CharField()
    gender = serializers.CharField()
    age = serializers.IntegerField()
    height=serializers.DecimalField(max_digits=10,decimal_places=2)
    weight=serializers.DecimalField(max_digits=10,decimal_places=2)
    marital_status=serializers.CharField(required=False)
    blood_group = serializers.CharField()
    ph_no=serializers.CharField()
    loggedInuser=serializers.IntegerField(required=False)
    profile_pic=serializers.FileField(required=False)

    def create(self, validated_data):
        try:
            
            user = User.objects.get(id=validated_data["loggedInuser"])
            patient = patient_info.objects.get(user__id=user.id)
            print(validated_data)
            user.username=validated_data['username']
            user.email=validated_data['email']
            for key,value in validated_data.items():
                if key!='pat_id':
                    setattr(patient,key,value)
            patient.save()
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

class UserEmail(serializers.ModelSerializer):
    class Meta:
        model=User            
        fields = ['email']


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()
    loggedInuser = serializers.IntegerField(required=False)

    def create(self, validated_data):
        # getting the user
        user = User.objects.get(id = validated_data['loggedInuser'])
        password = validated_data['old_password']
        # Check if the user's typed password is correct or not
        if user.check_password(password):
            # checking new two password is same or not.
            if validated_data['new_password'] == validated_data['confirm_new_password']:
                # set new password to the user.
                print(validated_data['new_password'])
                user.set_password(validated_data['new_password'])
                user.save()
                return user
            raise serializers.ValidationError("Your new passwords is not matched.")

        raise serializers.ValidationError("Your password is wrong. Please provide us right password") 

