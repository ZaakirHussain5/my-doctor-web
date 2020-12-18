from rest_framework import serializers
from .models import consultations
from doctors.serializers import doctors_infoSerializer
from accounts.serializers import UserAuthSerializer
from patients.models import patient_info

class consultationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = consultations
        fields = '__all__'
        read_only_fields = ('patient', 'doctor_id', 'comp_share', 'consultation_amt', 'duration')
        optional_fields = ['message', ]

class getAllConsultationsSerializer(serializers.ModelSerializer):
    doctor_id = doctors_infoSerializer()
    patient = UserAuthSerializer()
    patient_pic = serializers.SerializerMethodField('get_patient_pic')

    def get_patient_pic(self, obj):
        pat_details = patient_info.objects.get(user__id=obj.patient.id)
        if pat_details.profile_pic:
            return self.context['request'].build_absolute_uri(pat_details.profile_pic.url)
        return ""

    class Meta:
        model = consultations
        fields = ('id','doctor_id','patient','patient_name','patient_age','patient_gender','patient_pic','consultation_date_time','message',
            'inv_number', 'video_audio_rating', 'consultation_rating', 'overall_rating', 'consultation_amt','patient_number'
            )