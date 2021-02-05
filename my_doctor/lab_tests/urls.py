from django.urls import path, include
from rest_framework import routers

from .api import ( lab_testsViewset, lab_tests_parameters_type_viewset, lab_tests_parameter_viewset, 
    lab_tests_faqs_viewset,lab_tests_puchase_viewset, lab_test_files

)

router = routers.DefaultRouter()
router.register('labtestCRUD', lab_testsViewset, 'labtestCRUD')
router.register('labtestparameterTypeCRUD', lab_tests_parameters_type_viewset, 'labtestCRUD')
router.register('labtestparameterCRUD', lab_tests_parameter_viewset, 'labtestCRUD')
router.register('labtestFaqsCRUD', lab_tests_faqs_viewset, 'labtestCRUD')
router.register('PurchaseLabTests', lab_tests_puchase_viewset, 'PurchaseLabTests')
router.register('lab_test_files', lab_test_files, 'lab_test_files')
#router.register('LabTestsOrdersList', lab_tests_puchase_viewset, 'PurchaseLabTests')

urlpatterns = [
    path('', include(router.urls))
]



