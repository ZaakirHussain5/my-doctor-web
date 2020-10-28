from .api import vedioChatOparetion,InitiateCallAPI
from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register('vedioChatOparetion', vedioChatOparetion, 'vedioChatOparetion')

urlpatterns = [
    path('',include(router.urls)),
    path('createVideoSession',views.createVideoSession,name='sessionID'),
    path('getDoctorToken',views.getDoctorToken,name="DoctorToken"),
    path('videoCall',InitiateCallAPI.as_view(),name='VideoCall'),
    path('PatinetVideoUI',views.patientVideoChat,name="video_chat"),
    path('DoctorVideoUI',views.doctorVideoChat,name="video_chat")
]