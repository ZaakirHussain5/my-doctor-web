from django.shortcuts import render
from django.http import JsonResponse
from doctors.models import doctors_info
from patients.models import patient_info
from consultations.models import consultations
from patient_medical_records.models import patient_medical_records
from .models import VedioChat
from opentok import OpenTok,MediaModes
from django.db.models import Q 

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
    context = {}
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
        print(patient)
        consulation_list = consultations.objects.filter(patient=patient.user)
        medical_record = patient_medical_records.objects.filter(patient=patient.user)
        context['medical_records'] = medical_record
        context['consultation_lists'] = consulation_list
    # else:
    #     context['medical_records'] = []
    #     context['consultation_lists'] = []
    context['user'] =  user
    context['doctor']=doctor
    context['patient'] = patient
    context['session'] = session
    context['appointment'] = request.GET.get('appointment', None)
    
    return render(request,'video_chat/new_video_chat.html', context)

def ratings(request):

    return render(request,'video_chat/ratings.html', {'consultation': request.GET.get('consultation')})


