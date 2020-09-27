from rest_framework import routers
from django.urls import path,include

from patient_medical_records.api import PatientMedicalRecordView

router = routers.DefaultRouter()
router.register('patient-medical-records', PatientMedicalRecordView , 'patient-medical-records')

urlpatterns = [
    path('',include(router.urls)),
]