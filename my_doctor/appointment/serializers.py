from rest_framework import serializers
from .models import appointment
from doctors.serializers import doctors_infoSerializer
from accounts.serializers import UserAuthSerializer
from patients.models import patient_info

class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'


class cancleAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'
        read_only_fields = ('appointment_date', 'appointment_time', 'doctor', 'paid_amount')



class appointmentsListSerializer(serializers.ModelSerializer):
    doctor = doctors_infoSerializer()
    patient = UserAuthSerializer()
    # patient_pic = serializers.SerializerMethodField('get_patient_pic')

    # def get_patient_pic(self, obj):
    #     pat_details = patient_info.objects.get(user=obj.patient)
    #     if pat_details.profile_pic:
    #         return self.context['request'].build_absolute_uri(pat_details.profile_pic.url)
    #     return ""

    class Meta:
        model = appointment
        fields = ('id','doctor','patient','paid_amount', 'patient_name','patient_age','patient_gender','appointment_date','appointment_time','Description','pat_id','patient_login_status')