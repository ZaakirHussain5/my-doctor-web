from rest_framework import serializers

from .models import *

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


        