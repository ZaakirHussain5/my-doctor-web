from rest_framework import routers
from .api import consultationsViewSet,getAllConsultations,getPatientConsultations
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('consultations', consultationsViewSet, 'consultations')
router.register('getAllConsultations', getAllConsultations, 'getAllConsultations')
router.register('getPatientConsultations', getPatientConsultations, 'getPatientConsultations')

urlpatterns = [
    path('',include(router.urls)),
    path('getInvoiceNumber',views.generateId,name='getInvoiceNumber')
]