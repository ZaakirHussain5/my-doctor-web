from .api import MobRejectEndCallAPI, MobVedioChatOparetion,vedioChatOparetion, check_for_answer,call_doctor_mobile,MobAnswerCallAPI,call_patient_mobile
from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('vedioChatOparetion', vedioChatOparetion, 'vedioChatOparetion')
router.register('MobVedioChatOparetion', MobVedioChatOparetion, 'MobvedioChatOparetion')
router.register('check_for_answer', check_for_answer, 'check_for_answer')

urlpatterns = [
    path('',include(router.urls)),
    path('createVideoSession',views.createVideoSession,name='sessionID'),
    path('getDoctorToken',views.getDoctorToken,name="DoctorToken"),
    path('VideoCall',views.patientVideoChat,name="video_chat"),
    path('ratings',views.ratings,name='ratings'),
    path('reject_call',MobRejectEndCallAPI.as_view(),name='answer_call'),
    path('MobCallDoctor',call_doctor_mobile.as_view(),name='MDVideoCall'),
    path('MobCallPatient',call_patient_mobile.as_view(),name='MPVideoCall'),
    path('MobAnswerCall',MobAnswerCallAPI.as_view(),name='answer_call'),
]