from rest_framework import routers
from .api import (consultationsViewSet,getAllConsultations,getPatientConsultations,getDoctorConsultations, 
    specific_patient_consultations, consult_info_for_doct,GetConsultationDetails)
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('consultations', consultationsViewSet, 'consultations')
router.register('specific_patient_consultations', specific_patient_consultations, 'specific_patient_consultations')
router.register('getAllConsultations', getAllConsultations, 'getAllConsultations')
router.register('getPatientConsultations', getPatientConsultations, 'getPatientConsultations')
router.register('getDoctorConsultations', getDoctorConsultations, 'getDoctorConsultations')
router.register('consult_info_for_doct', consult_info_for_doct, 'consult_info_for_doct')

urlpatterns = [
    path('',include(router.urls)),
    path('getInvoiceNumber',views.generateId,name='getInvoiceNumber'),
    path('getConsDetails',GetConsultationDetails.as_view(),name='getConsDetails')
]