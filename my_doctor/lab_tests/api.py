from rest_framework import viewsets, permissions, status


from .serializer import *
from patients.models import patient_info

class lab_testsViewset(viewsets.ModelViewSet):
    queryset = lab_tests.objects.all()
    serializer_class = lab_testsSerializer
    permissions = [
        permissions.AllowAny
    ]



class lab_tests_parameters_type_viewset(viewsets.ModelViewSet):
    serializer_class = lab_tests_parameters_type_serializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = lab_tests_parameters_type.objects.all()
        lab_test = self.request.query_params.get('labtest',None)
        if lab_test is not None:
            queryset = lab_tests_parameters_type.objects.filter(lab_test__id=lab_test)
        return queryset


class lab_tests_parameter_viewset(viewsets.ModelViewSet):
    serializer_class = lab_tests_parameter_serializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = lab_tests_parameter.objects.all()
        parameter_type = self.request.query_params.get('type',None)
        if parameter_type is not None:
            queryset = lab_tests_parameter.objects.filter(parameter_type__id=parameter_type)
        return queryset
        


class lab_tests_faqs_viewset(viewsets.ModelViewSet):
    serializer_class = lab_tests_faqs_serializer
    permissions=[permissions.AllowAny]

    def get_queryset(self):
        queryset = lab_tests_faqs.objects.all()
        lab_test = self.request.query_params.get('labtest',None)
        if lab_test is not None:
            queryset = lab_tests_faqs.objects.filter(lab_test__id=lab_test)
        return queryset

class lab_tests_puchase_viewset(viewsets.ModelViewSet):
    serializer_class = lab_tests_purchase_serializer
    permissions=[permissions.AllowAny]

    def perform_create(self,serializer):
        user_id = patient_info.objects.get(user=self.request.user)
        return serializer.save(user_id=user_id)
    
    def get_queryset(self):
        self.serializer_class = lab_tests_purchase_list_serializer
        queryset = lab_tests_purchase.objects.all()
        if self.request.user.is_authenticated:
            queryset = lab_tests_purchase.objects.filter(user_id=patient_info.objects.get(user=self.request.user))
        return queryset


class lab_test_files(viewsets.ModelViewSet):
    serializer_class = FilesSerializer
    permissions = [permissions.AllowAny]

    def get_queryset(self):
        queryset = lab_test_perches_files.objects.all()
        get_id = self.request.query_params.get('id')
        if get_id is not None:
            queryset = lab_test_perches_files.objects.filter(purchase__id=get_id)
        return queryset
    