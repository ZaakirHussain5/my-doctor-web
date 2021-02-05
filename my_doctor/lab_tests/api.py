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
    queryset = lab_tests_parameters_type.objects.all()
    serializer_class = lab_tests_parameters_type_serializer
    permission_classes = [permissions.AllowAny]


class lab_tests_parameter_viewset(viewsets.ModelViewSet):
    queryset = lab_tests_parameter.objects.all()
    serializer_class = lab_tests_parameter_serializer
    permission_classes = [permissions.AllowAny]


class lab_tests_faqs_viewset(viewsets.ModelViewSet):
    queryset = lab_tests_faqs.objects.all()
    serializer_class = lab_tests_faqs_serializer
    permissions=[permissions.AllowAny]

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
        get_id = self.request.query_params.get('id')
        purches = lab_tests_purchase.objects.get(id=get_id)
        print(purches)
        return lab_test_perches_files.objects.filter(purchase=purches)
    