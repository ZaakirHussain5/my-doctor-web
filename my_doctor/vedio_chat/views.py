from django.shortcuts import render
from django.http import JsonResponse
from doctors.models import doctors_info
from patients.models import patient_info
from consultations.models import consultations
from patient_medical_records.models import patient_medical_records
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
    user = request.GET.get('user')
    doctor_id = request.GET.get('doctor')
    patient_id = request.GET.get('patient')
    session = request.GET.get('session')
    doctor,patient = None,None
    consulation_list = None
    if doctor_id is not None:
        doctor = doctors_info.objects.get(pk=doctor_id)
    if patient_id is not None:
        patient = patient_info.objects.get(pk=patient_id)
        consulation_list = consultations.objects.filter(patient__user=patient.user)
        medical_records = medical_records.objects.filter()
    return render(request,'video_chat/video_chat.html',{"user" : user,"doctor":doctor,"patient":patient,"session":session})

def ratings(request):
    return render(request,'video_chat/ratings.html')


