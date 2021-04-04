from rest_framework import permissions,viewsets, mixins,generics
from rest_framework.response import Response
from .models import VedioChat,video_chat_session
from .serializers import VedioChatSerializer,video_mobile_serializer
from doctors.models import doctors_info
from patients.models import patient_info
from appointment.models import appointment as appo
from rest_framework import status
from opentok import OpenTok
opentok = OpenTok("47034434", "21f8951c03ab3c4f33eba0962905212594f477e5")

class vedioChatOparetion(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VedioChatSerializer

    def get_queryset(self):
        queryset = VedioChat.objects.filter(is_answered=False)
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = self.request.user.call_for.filter(is_answered=False)
        return queryset
    
    def perform_create(self,serializer):
        return serializer.save()

class MobVedioChatOparetion(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = video_mobile_serializer

    def get_queryset(self):
        queryset = video_chat_session.objects.filter(is_answered=False)
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = self.request.user.call_for_user.filter(is_answered=False)
        return queryset
    
    def perform_create(self,serializer):
        return serializer.save()

    def perform_destroy(self,serializer):
        if self.request.user.id == serializer.Call_from.id:
          if serializer.Call_for.username.startswith('DPDOC') and serializer.is_answered == False:
            doctor = doctors_info.objects.get(user__id=serializer.Call_for.id)
            pushNotification(doctor.fcm_token,"Call Rejected","Call was Rejected by Patient")
          elif serializer.is_answered == False:
            patient = patient_info.objects.get(user__id=serializer.Call_for.id)
            pushNotification(patient.fcm_token,"Call Rejected","Call was rejected by the Doctor")
        else:
          if serializer.Call_from.username.startswith('DPDOC') and serializer.is_answered == False:
            doctor = doctors_info.objects.get(user__id=serializer.Call_from.id)
            pushNotification(doctor.fcm_token,"Call Rejected","Call was Rejected by Patient")
          elif serializer.is_answered == False:
            patient = patient_info.objects.get(user__id=serializer.Call_from.id)
            pushNotification(patient.fcm_token,"Call Rejected","Call was rejected by the Doctor")

        return serializer.delete()

class CallDoctorAPI(generics.GenericAPIView):
  serializer_class = VedioChatSerializer

  def post(self, request, *args, **kwargs):
    doctor_id = request.query_params.get('doctor_id',None)
    doctor = doctors_info.objects.get(id=doctor_id)
    appoinment = request.query_params.get('const', None)
    
    video = VedioChat.objects.create(Call_from=request.user,Call_for=doctor.user, appoinment_id=appoinment)
    video.save()
    return Response({
      "Message":"Call initiated",
      "id":video.id
    })


class AnswerCallAPI(generics.GenericAPIView):
  serializer_class = VedioChatSerializer
  
  def post(self, request, *args, **kwargs):
    session_id = request.query_params.get('session_id',None)
    video = VedioChat.objects.get(id=session_id)
    if video.Call_for == request.user:
      video.is_answered = True
      video.save()
      return Response({
        "Message":"Call Answered",
        "id":video.id
      })
    return Response(status=status.HTTP_400_BAD_REQUEST)


class CallPatientAPI(generics.GenericAPIView):
  serializer_class = VedioChatSerializer

  def post(self, request, *args, **kwargs):
    patient_id = request.query_params.get('patient',None)
    appoinment = request.query_params.get('const',None)
    patient = patient_info.objects.get(id=patient_id)
    video = VedioChat.objects.create(Call_from=request.user,Call_for=patient.user, appoinment_id=appoinment)
    video.save()
    return Response({
      "Message":"Call initiated",
      "id":video.id
    })


class check_for_answer(viewsets.ModelViewSet):
  serializer_class = VedioChatSerializer
  permissions = [
    permissions.IsAuthenticated
  ]

  def get_queryset(self):
    data = self.request.query_params.get('sessions', None)
    if data:
      return video_chat_session.objects.filter(id=data)
    return []

class call_patient_mobile(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  def post(self, request, *args, **kwargs):
    patient_id = request.query_params.get('patient',None)
    appointment = request.query_params.get('app_id',None)
    patient = patient_info.objects.get(id=patient_id)
    if patient.is_logged_in:
      session = opentok.create_session()
      session_id = session.session_id
      doctor_token = session.generate_token()
      appointIns=appo.objects.get(id=appointment)
      video = video_chat_session.objects.create(Call_from=request.user,Call_for=patient.user, appoinment_id=appointment,session_id=session_id,user_token=doctor_token)
      #pushNotification(patient.fcm_token,"Call From "+appointIns.doctor.name,"You are getting a call from your doctor for the Appointment.")
      return Response({
        "Message":"Call initiated",
        "session_id":session_id,
        "token":doctor_token,
        "id":video.id
      })
    else:
      return Response({
        "error":"Patient is Offline"
      })

class call_doctor_mobile(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  def post(self, request, *args, **kwargs):
    doctor_id = request.query_params.get('doctor',None)
    appointment = request.query_params.get('app_id',None)
    doctor = doctors_info.objects.get(id=doctor_id)
    if doctor.is_loggedin:
      session = opentok.create_session()
      session_id = session.session_id
      patient_token = session.generate_token()
      appointIns=appo.objects.get(id=appointment)
      video = video_chat_session.objects.create(Call_from=request.user,Call_for=doctor.user, appoinment_id=appointment,session_id=session_id,user_token=patient_token)
      #pushNotification(doctor.fcm_token,"Call From "+appointIns.patient_name,"You are getting a call from your patient for the Appointment.")
      return Response({
        "Message":"Call initiated",
        "session_id":session_id,
        "token":patient_token,
        "id":video.id
      })
    else:
      return Response({
        "error":"Doctor is Offline"
      })

class MobAnswerCallAPI(generics.GenericAPIView):
  serializer_class = video_mobile_serializer
  
  def post(self, request, *args, **kwargs):
    session_id = request.query_params.get('id',None)
    video = video_chat_session.objects.get(id=session_id)
    #if video.Call_for == request.user:
    video.is_answered = True
    video.save()
    token = opentok.generate_token(video.session_id)
    return Response({
        "Message":"Call Answered",
        "session_id" : video.session_id,
        "token":token
    })

def pushNotification(deviceToken,title, message):
    import requests
    import json

    serverToken = 'AIzaSyD5FJg-faFBfW53PhRIqYKzlJHzSlUTGXE'

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'key=' + serverToken
    }

    body = {
      'notification': {'title': title,'body': message},
      'to': deviceToken,
      'priority': 'high'
    }
    response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())

