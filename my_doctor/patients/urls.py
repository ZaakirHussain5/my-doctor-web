from rest_framework import routers
from .api import patient_infoViewSet,PatientResgistrationAPI
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('patient_info', patient_infoViewSet, 'patient_info')

urlpatterns = [
    path('',include(router.urls)),
    path('PatientResistration',PatientResgistrationAPI.as_view(),name='PatientResistration'),
    path('GeneratePatientID',views.generateId,name='GeneratePatientID')
]
