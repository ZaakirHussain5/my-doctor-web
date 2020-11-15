from .api import vedioChatOparetion,CallDoctorAPI,CallPatientAPI
from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register('vedioChatOparetion', vedioChatOparetion, 'vedioChatOparetion')

urlpatterns = [
    path('',include(router.urls)),
    path('createVideoSession',views.createVideoSession,name='sessionID'),
    path('getDoctorToken',views.getDoctorToken,name="DoctorToken"),
    path('CallDoctor',CallDoctorAPI.as_view(),name='DVideoCall'),
    path('CallPatient',CallPatientAPI.as_view(),name='PVideoCall'),
    path('VideoCall',views.patientVideoChat,name="video_chat"),
    path('ratings',views.ratings,name='ratings')
]