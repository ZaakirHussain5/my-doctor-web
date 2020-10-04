from rest_framework import routers
from .api import PatientUpdateProfileAPI, GetLoggedPatient,patient_infoViewSet,PatientResgistrationAPI,medical_historyViewSet,groupsViewSet,PatientResgistrationAppAPI, PatientEmail, PasswordChange
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('patient_info', patient_infoViewSet, 'patient_info')
router.register('medical_history', medical_historyViewSet, 'medical_history')
router.register('groups', groupsViewSet, 'groups')

urlpatterns = [
    path('',include(router.urls)),
    path('PatientRegistration',PatientResgistrationAPI.as_view(),name='PatientRegistration'),
    path('GeneratePatientID',views.generateId,name='GeneratePatientID'),
    path('PatientRegInApp',PatientResgistrationAppAPI.as_view(),name='PatientRegInApp'),
    path('getLoggedInPatient',GetLoggedPatient.as_view(),name='getLoggedInPatient'),
    path('PatientUpdateProfile',PatientUpdateProfileAPI.as_view(),name='PatientUpdateProfile'),
    path('getEmail', PatientEmail.as_view(), name='PatientEmail'),
    path('changePassword', PasswordChange.as_view(), name='Password_change'),
]
