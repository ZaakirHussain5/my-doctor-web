from rest_framework import routers
from .api import (PatientUpdateProfileAPI, GetLoggedPatient,patient_infoViewSet,PatientResgistrationAPI,
    medical_historyViewSet,groupsViewSet,PatientResgistrationAppAPI, PatientEmail, PasswordChange,
    PatientBillingHistorys, patientData, SpecificPatient_infoViewSet,PatientLogout,patient_family_membersViewset,
    socialPatientRegistrationView, check_phone_no, cheange_password
)
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register('patient_info', patient_infoViewSet, 'patient_info')
router.register('SpecificPatient_infoViewSet', SpecificPatient_infoViewSet, 'SpecificPatient_infoViewSet')
router.register('medical_history', medical_historyViewSet, 'medical_history')
router.register('patient_family', patient_family_membersViewset, 'patient_family')
router.register('PatientBillingHistory', PatientBillingHistorys, 'PatientBillingHistory')


urlpatterns = [
    path('',include(router.urls)),
    path('PatientRegistration',PatientResgistrationAPI.as_view(),name='PatientRegistration'),
    path('GeneratePatientID',views.generateId,name='GeneratePatientID'),
    path('PatientRegInApp',PatientResgistrationAppAPI.as_view(),name='PatientRegInApp'),
    path('socialPatientRegistrationView/', socialPatientRegistrationView.as_view(), name = 'socialPatientRegistrationView'),
    path('getLoggedInPatient',GetLoggedPatient.as_view(),name='getLoggedInPatient'),
    path('PatientUpdateProfile',PatientUpdateProfileAPI.as_view(),name='PatientUpdateProfile'),
    path('getEmail', PatientEmail.as_view(), name='PatientEmail'),
    path('changePassword', PasswordChange.as_view(), name='Password_change'),
    path('detailsOfPatient', patientData, name="FullDetails"),
    path('PatientLogout',PatientLogout.as_view(),name='LogoutPatient'),
    path('patient_check_phone/', check_phone_no.as_view(), name="check_phone_no"),
    path('reset_forget_password/', cheange_password.as_view(), name="reset_password")
]
