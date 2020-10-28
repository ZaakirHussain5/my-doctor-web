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
<<<<<<< HEAD
    path('PatientVideoUI',views.patientVideoChat,name="video_chat"),
    path('DoctorVideoUI',views.doctorVideoChat,name="video_chat"),
    path('ratings',views.ratings,name='ratings')
=======
    path('PatinetVideoUI',views.patientVideoChat,name="video_chat"),
    path('DoctorVideoUI',views.doctorVideoChat,name="video_chat")
>>>>>>> f46f170114a7cb77da023a77f5d8842d519bd0da
]