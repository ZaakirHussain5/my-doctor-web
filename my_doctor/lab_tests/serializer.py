from rest_framework import serializers

from .models import *
from patients.serializers import patient_infoSerializer

class lab_testsSerializer(serializers.ModelSerializer):
    class Meta:
        model = lab_tests
        fields = '__all__'


class lab_tests_parameters_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = lab_tests_parameters_type
        fields = '__all__'


class lab_tests_parameter_serializer(serializers.ModelSerializer):
    class Meta:
        model = lab_tests_parameter
        fields = '__all__'


class lab_tests_faqs_serializer(serializers.ModelSerializer):
    class Meta:
        model = lab_tests_faqs
        fields = '__all__'

class lab_tests_purchase_serializer(serializers.ModelSerializer):
    class Meta:
        model = lab_tests_purchase
        fields = '__all__'
        extra_kwargs = {'user_id':{'required':False}}

class lab_tests_purchase_list_serializer(serializers.ModelSerializer):
    user_id = patient_infoSerializer()
    lab_test_id = lab_testsSerializer()

    class Meta:
        model = lab_tests_purchase
        fields = '__all__'

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = lab_test_perches_files
        fields = '__all__'


        