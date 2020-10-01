from rest_framework import routers
from .api import DoctorUpdateProfileAPI, GetLoggedDoctor,DoctorTimingsAPI,doctors_infoViewSet,DoctorRegisterAPI,getAvailableDoctors
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('doctors_info', doctors_infoViewSet, 'doctors_info')
router.register('getAvailableDoctors', getAvailableDoctors, 'getAvailableDoctors')
router.register('DoctorTimings',DoctorTimingsAPI,'DoctorTimings')

urlpatterns = [
    path('',include(router.urls)),
    path('DoctorRegistration/',DoctorRegisterAPI.as_view(),name='DoctorRegistration'),
    path('GenerateDoctorID',views.generateId,name='GenerateDoctorID'),
    path('getLoggedInDoctor',GetLoggedDoctor.as_view(),name='getLoggedInDoctor'),
    path('DoctorUpdateProfile',DoctorUpdateProfileAPI.as_view(),name='DoctorUpdateProfile'),
]
