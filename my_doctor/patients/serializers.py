from rest_framework import serializers
from .models import patient_info,medical_history,groups, PatientBillingHistory,patient_family_members
from django.contrib.auth.models import User
from django.db import IntegrityError
from accounts.models import user_details

class patient_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient_info
        fields = '__all__'
        depth= 1

class PatientResgistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    pat_id = serializers.CharField()
    full_name = serializers.CharField()
    gender = serializers.CharField(required=False)
    # dob = serializers.CharField(allow_blank=True,allow_null=True)
    age = serializers.IntegerField(required=False)
    blood_group = serializers.CharField(allow_blank=True,allow_null=True)
    rel_type = serializers.CharField(allow_blank=True,allow_null=True)
    relation = serializers.CharField(allow_blank=True,allow_null=True)
    ph_no=serializers.CharField()
    s_ph_no=serializers.CharField(allow_blank=True,allow_null=True)
    pref_lang = serializers.CharField(allow_blank=True,allow_null=True)
    street_address = serializers.CharField(allow_blank=True,allow_null=True)
    # locality = serializers.CharField(allow_blank=True,allow_null=True)
    city = serializers.CharField(allow_blank=True,allow_null=True)
    # pincode=serializers.CharField(allow_blank=True,allow_null=True)
    medical_history = serializers.CharField(allow_blank=True,allow_null=True)
    other_history=serializers.CharField(required=False, allow_blank=True, allow_null=True)
    groups=serializers.CharField(allow_blank=True,allow_null=True)
    profile_pic=serializers.FileField(required=False)

    def create(self, validated_data):
        try:
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
            patient_details = patient_info.objects.create(user=user,
            pat_id=validated_data['pat_id'],
            full_name=validated_data['full_name'],
            gender=validated_data.get('gender', None),
            dob=validated_data.get('dob', None),
            age=validated_data.get('age', None),
            blood_group=validated_data.get('blood_group', None),
            rel_type=validated_data.get('rel_type', None),
            relation=validated_data.get('relation', None),
            ph_no=validated_data['ph_no'],
            s_ph_no=validated_data.get('s_ph_no',None),
            pref_lang=validated_data.get('pref_lang', None),
            street_address = validated_data.get('street_address', None),
            locality = validated_data.get('locality', None),
            city = validated_data.get('city', None),
            pincode = validated_data.get('pincode', None),
            medical_history = validated_data.get('medical_history', None),
            groups = validated_data.get('groups', None),
            profile_pic = validated_data.get('profile_pic', None),
            other_history = validated_data.get('other_history', None)
            )
            patient_details.save()
            # if "other_history" in validated_data:
            #     other_history = validated_data['other_history']
            #     patient_details.other_history = other_history
            #     patient_details.save()
            return user
        except IntegrityError:
            raise serializers.ValidationError("User Already Exists")


class socailRegistrationSerializer(serializers.Serializer):
    email = serializers.CharField()
    pat_id = serializers.CharField()
    full_name = serializers.CharField()

    def create(self, validated_data):
        try:
            user = User.objects.get(username = validated_data['email'])
        except User.DoesNotExist:
            user = User(username=validated_data['email'], email=validated_data['email'])
            user.save()
            patient_details = patient_info.objects.create(user=user,
                pat_id=validated_data['pat_id'],
                full_name=validated_data['full_name']
            )
        return user


class PatientResgistrationApp(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField(required=False,allow_blank=True,allow_null=True)
    pat_id = serializers.CharField()
    full_name = serializers.CharField()
    fcm_token = serializers.CharField(required=False,allow_blank=True,allow_null=True)

    def create(self, validated_data):
        try:
            user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
            patient_details = patient_info.objects.create(user=user,
            pat_id=validated_data['pat_id'],
            full_name=validated_data['full_name'],
            ph_no=validated_data['username'],
            fcm_token=validated_data["fcm_token"])
            patient_details.save()
            return user
        except IntegrityError:
            raise serializers.ValidationError("User Already Exists")


class UpdateProfile(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.CharField(allow_null=True,allow_blank=True)
    full_name = serializers.CharField()
    age = serializers.IntegerField(required=False)
    weight=serializers.DecimalField(max_digits=10,decimal_places=2,required=False)
    blood_group = serializers.CharField(required=False)
    ph_no=serializers.CharField()
    loggedInuser=serializers.IntegerField(required=False)
    profile_pic=serializers.FileField(required=False)

    def create(self, validated_data):
        try:
            user = User.objects.get(id=validated_data["loggedInuser"])
            patient = patient_info.objects.get(user__id=user.id)
            print(validated_data)
            user.username=validated_data.get('username', user.username)
            user.email=validated_data['email']
            user.save()
            patient.user = user
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

class patient_family_membersSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient_family_members
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

class PatientBillingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientBillingHistory
        fields= '__all__'
        read_only_fields = ('patient', )