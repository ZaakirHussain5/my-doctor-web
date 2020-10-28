from django.shortcuts import render
from django.http import JsonResponse
from doctors.models import doctors_info
from .models import VedioChat
from opentok import OpenTok,MediaModes
opentok = OpenTok("46964534", "76ca83ec02f7c0ef904f536a2d0bc251df25d8a4")

def createVideoSession(request):
    session = opentok.create_session(media_mode=MediaModes.routed)
    return JsonResponse({
        "session_id":session.session_id})

def getDoctorToken(request):
    session_id = request.GET.get('session_id')
    print(session_id)
    return JsonResponse({
        "token":opentok.generate_token(session_id)
    })

def patientVideoChat(request):
    return render(request,'video_chat/patient_video_ui.html')

def doctorVideoChat(request):
    return render(request,'video_chat/doctor_video_ui.html')


