from rest_framework import viewsets, permissions, status


from .serializer import *

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

    