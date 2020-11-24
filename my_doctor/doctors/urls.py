from rest_framework import routers
from .api import (DoctorUpdateProfileAPI, GetLoggedDoctor,DoctorTimingsAPI,
                  doctors_infoViewSet,DoctorRegisterAPI,getAvailableDoctors,
                  NewDoctorRegistration, webdoctorViewset, get_settlement_details,
                  get_doctor_bankDetails, doctor_agreement_list, doctorRegistrationAdmin,
                  DoctorTimingsAdminAPI, specificDoctorSettlement, doctor_info_adminViewSet, 
                  getAvailableDoctorsForApponment, changeFee, doctor_bankDetails, changeFeeByAdmin,
                  DoctorLogout, DoctorUpdateProfileAdminAPI, DoctorTimingsApiView, doctor_bankDetailsAdminView, doctor_notesView)
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('doctors_info', doctors_infoViewSet, 'doctors_info')
router.register('doctor_info_admin', doctor_info_adminViewSet, 'doctor_info_admin')
router.register('getAvailableDoctors', getAvailableDoctors, 'getAvailableDoctors')
router.register('patientAppointment/DoctorAvailable', getAvailableDoctorsForApponment, 'getAvailableDoctorsForApponment')
router.register('DoctorTimings',DoctorTimingsAPI,'DoctorTimings')
router.register('DoctorTimingsApiView',DoctorTimingsApiView,'DoctorTimingsApiView')
router.register('DoctorTimingsAdminAPI',DoctorTimingsAdminAPI,'DoctorTimingsAdminAPI')
router.register('webDorRegistrationList',webdoctorViewset,'DoctorTimings')
router.register('get_settlement_details',get_settlement_details,'get_settlement_details')
router.register('doctor_bank_details', get_doctor_bankDetails,'get_settlement_details')
router.register('doctor_agreement_list', doctor_agreement_list,'get_settlement_details')
router.register('specificDoctorPaymentList', specificDoctorSettlement, 'specificDoctorSettlement')
router.register('doctor_bankDetails', doctor_bankDetails,'doctor_bankDetails')
router.register('doctor_bankDetailsAdminView', doctor_bankDetailsAdminView,'doctor_bankDetailsAdminView')
router.register('doctor_notesView', doctor_notesView,'doctor_notesView')


urlpatterns = [
    path('',include(router.urls)),
    path('DoctorRegistration/',DoctorRegisterAPI.as_view(),name='DoctorRegistration'),
    path('GenerateDoctorID',views.generateId,name='GenerateDoctorID'),
    path('getLoggedInDoctor',GetLoggedDoctor.as_view(),name='getLoggedInDoctor'),
    path('DoctorUpdateProfile',DoctorUpdateProfileAPI.as_view(),name='DoctorUpdateProfile'),
    path('DoctorUpdateProfileAdminAPI',DoctorUpdateProfileAdminAPI.as_view(),name='DoctorUpdateProfileAdminAPI'),
    path('doctor_registrationByAdmin/',doctorRegistrationAdmin.as_view(),name='doctor_registrationByAdmin'),
    path("NewDoctorRegistration", NewDoctorRegistration.as_view(), name="newDoctorRegistration"),
    path('changeFee/', changeFee.as_view(), name = 'changeFee'),
    path('changeFeeByAdmin/', changeFeeByAdmin.as_view(), name = 'changeFeeByAdmin'),
    path('DoctorLogout',DoctorLogout.as_view(),name="logoutDoctor")
]
