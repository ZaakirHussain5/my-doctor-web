from rest_framework import routers
from .api import consultationsViewSet,getAllConsultations,getPatientConsultations,getDoctorConsultations
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('consultations', consultationsViewSet, 'consultations')
router.register('getAllConsultations', getAllConsultations, 'getAllConsultations')
router.register('getPatientConsultations', getPatientConsultations, 'getPatientConsultations')
router.register('getDoctorConsultations', getDoctorConsultations, 'getDoctorConsultations')

urlpatterns = [
    path('',include(router.urls)),
    path('getInvoiceNumber',views.generateId,name='getInvoiceNumber')
]