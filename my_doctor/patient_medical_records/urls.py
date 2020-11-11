from rest_framework import routers
from django.urls import path,include

from .api import ( getAllPrescriptions, PatientMedicalRecordView,PatientPrescriptionAPI,
        DoctorPrescriptionAPI, DoctorPrescriptionAPIDelete, PatientRecordAPI,  

)

router = routers.DefaultRouter()
router.register('patient-medical-records', PatientMedicalRecordView , 'patient-medical-records')
router.register('DoctorPrescription', DoctorPrescriptionAPI , 'DoctorPrescription')
router.register('DoctorPrescriptionDelete', DoctorPrescriptionAPIDelete , 'DoctorPrescription')
router.register('PatientPrescription', PatientPrescriptionAPI , 'PatientPrescription')
router.register('getAllPrescriptions', getAllPrescriptions , 'getAllPrescriptions')
router.register('PatientRecordAPI', PatientRecordAPI , 'PatientRecordAPI')


urlpatterns = [
    path('',include(router.urls)),
]