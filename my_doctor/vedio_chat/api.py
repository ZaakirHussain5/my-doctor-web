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
        queryset = video_chat_session.objects.filter(is_answered=False).filter(is_rejected=False)
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = self.request.user.call_for_user.filter(is_answered=False).filter(is_rejected=False)
        return queryset
    
    def perform_create(self,serializer):
        return serializer.save()



class check_for_answer(viewsets.ModelViewSet):
  serializer_class = VedioChatSerializer
  permissions = [
    permissions.IsAuthenticated
  ]

  def get_queryset(self):
    data = self.request.query_params.get('sessions', None)
    if data:
      return video_chat_session.objects.filter(id=data).filter(is_rejected=False)
    return []

class call_patient_mobile(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  permissions = [
    permissions.IsAuthenticated
  ]
  def post(self, request, *args, **kwargs):
    patient_id = request.query_params.get('patient',None)
    appointment = request.query_params.get('app_id',None)
    patient = patient_info.objects.get(id=patient_id)
    if patient.is_logged_in:
      session = opentok.create_session()
      session_id = session.session_id
      doctor_token = session.generate_token()
      appointIns=appo.objects.get(id=appointment)
      pushNotification(patient.fcm_token,"Call From "+appointIns.doctor.full_name,"You are getting a call from your doctor for the Appointment.","P")
      video = video_chat_session.objects.create(Call_from=request.user,Call_for=patient.user, appoinment_id=appointment,session_id=session_id,user_token=doctor_token)
      return Response({
        "Message":"Call initiated",
        "session_id":session_id,
        "token":doctor_token,
        "id":video.id
      })
    else:
      return Response({
        "error":"Patient is Offline"
      },status=status.HTTP_400_BAD_REQUEST)

class call_doctor_mobile(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  permissions = [
    permissions.IsAuthenticated
  ]

  def post(self, request, *args, **kwargs):
    doctor_id = request.query_params.get('doctor',None)
    appointment = request.query_params.get('app_id',None)
    doctor = doctors_info.objects.get(id=doctor_id)
    if doctor.is_loggedin:
      session = opentok.create_session()
      session_id = session.session_id
      patient_token = session.generate_token()
      appointIns=appo.objects.get(id=appointment)
      pushNotification(doctor.fcm_token,"Call From "+appointIns.patient_name,"You are getting a call from your patient for the Appointment.","D")
      video = video_chat_session.objects.create(Call_from=request.user,Call_for=doctor.user, appoinment_id=appointment,session_id=session_id,user_token=patient_token)
      return Response({
        "Message":"Call initiated",
        "session_id":session_id,
        "token":patient_token,
        "id":video.id
      })
    else:
      return Response({
        "error":"Doctor is Offline"
      },status=status.HTTP_400_BAD_REQUEST)

class MobAnswerCallAPI(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  permissions = [
    permissions.IsAuthenticated
  ]
  
  def post(self, request, *args, **kwargs):
    try:
      video = video_chat_session.objects.get(Call_for=request.user,is_answered=False,is_rejected=False)
    except video_chat_session.DoesNotExist:
      return Response({"error":"No Active Calls found"},status=status.HTTP_400_BAD_REQUEST)
    video.is_answered = True
    video.save()
    token = opentok.generate_token(video.session_id)
    return Response({
        "Message":"Call Answered",
        "session_id" : video.session_id,
        "token":token
    })

class MobRejectEndCallAPI(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  permissions = [
    permissions.IsAuthenticated
  ]
  
  def post(self, request, *args, **kwargs):
    try:
      video = video_chat_session.objects.get(Call_for=request.user,is_answered=False,is_rejected=False)
    except video_chat_session.DoesNotExist:
      try:
        video = video_chat_session.objects.get(Call_from=request.user,is_rejected=False)
      except video_chat_session.DoesNotExist:
        try:  
          video = video_chat_session.objects.get(Call_for=request.user,is_rejected=False)
        except video_chat_session.DoesNotExist:
          return Response({"error":"No Active Calls found"},status=status.HTTP_400_BAD_REQUEST)

    video.is_rejected = True
    video.save()
    if request.user.id == video.Call_from.id:
      if video.Call_for.username.startswith('DPDOC') and video.is_answered == False:
        doctor = doctors_info.objects.get(user__id=video.Call_for.id)
        pushNotification(doctor.fcm_token,"Call Ended","Call was Ended by Patient","D")
      elif serializer.is_answered == False:
        patient = patient_info.objects.get(user__id=video.Call_for.id)
        pushNotification(patient.fcm_token,"Call Ended","Call was Ended by the Doctor","P")
    else:
      if video.Call_from.username.startswith('DPDOC') and video.is_answered == False:
        doctor = doctors_info.objects.get(user__id=video.Call_from.id)
        pushNotification(doctor.fcm_token,"Call Rejected","Call was Rejected by Patient","D")
      elif video.is_answered == False:
        patient = patient_info.objects.get(user__id=video.Call_from.id)
        pushNotification(patient.fcm_token,"Call Rejected","Call was rejected by the Doctor","P")
    return Response({
        "Message":"Call Rejected"
    })

class MobEndCallAPI(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  permissions = [
    permissions.IsAuthenticated
  ]
  
  def post(self, request, *args, **kwargs):
    try:
      video = video_chat_session.objects.get(Call_for=request.user,is_answered=False,is_rejected=False)
    except video_chat_session.DoesNotExist:
      video = video_chat_session.objects.get(Call_from=request.user,is_answered=False,is_rejected=False)
    video.is_ended = True
    video.save()
    if request.user.id == video.Call_from.id:
      if video.Call_for.username.startswith('DPDOC') and video.is_answered == False:
        doctor = doctors_info.objects.get(user__id=video.Call_for.id)
        pushNotification(doctor.fcm_token,"Call Rejected","Call was Rejected by Patient","D")
      elif serializer.is_answered == False:
        patient = patient_info.objects.get(user__id=video.Call_for.id)
        pushNotification(patient.fcm_token,"Call Rejected","Call was rejected by the Doctor","P")
    else:
      if video.Call_from.username.startswith('DPDOC') and video.is_answered == False:
        doctor = doctors_info.objects.get(user__id=video.Call_from.id)
        pushNotification(doctor.fcm_token,"Call Rejected","Call was Rejected by Patient","D")
      elif video.is_answered == False:
        patient = patient_info.objects.get(user__id=video.Call_from.id)
        pushNotification(patient.fcm_token,"Call Rejected","Call was rejected by the Doctor","P")
    return Response({
        "Message":"Call Rejected"
    })

def pushNotification(deviceToken,title, message,user):
    import requests
    import json

    if user == "D" :
      serverToken = 'AAAA08jY3gQ:APA91bE_y6faaIH3lej5TUBUuM2z4dIO4hUIWJ_HF1OVOsEdtiSQS9Dmyp8hRaHInFYImiqLp1OjxwcVngI_q0IwAexzUwfT9mobnsVDkegygwgYdF4_afgNmgDpy5jHMWMCWbl5Q-X-'
    else:
      serverToken = 'AAAAYWuqYoM:APA91bFkyQr5rD92Zd6IB1-5O6QnQRcFYCFvAENEdushl7f2RxSRR45qVno1UDsNGHvGIJfGBAukqnol2XSSWyBnoigdoqarb7-Hu7CshYtPyduu5IHR4FKcU_nJGPWq0NjwHIfZYWSX'

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'key=' + serverToken
    }

    body = {
      'data': {'title': title,'message': message,"action":"1"},
      'to': deviceToken,
    }
    response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response.status_code)

    print(response)

