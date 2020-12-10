from rest_framework import permissions,viewsets, mixins,generics
from rest_framework.response import Response
from .models import VedioChat,video_chat_session
from .serializers import VedioChatSerializer,video_mobile_serializer
from doctors.models import doctors_info
from patients.models import patient_info
from rest_framework import status
from opentok import OpenTok
opentok = OpenTok("47034434", "21f8951c03ab3c4f33eba0962905212594f477e5")

class vedioChatOparetion(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
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
      return VedioChat.objects.filter(id=data)
    return False

class call_patient_mobile(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  def post(self, request, *args, **kwargs):
    patient_id = request.query_params.get('patient',None)
    appoinment = request.query_params.get('app_id',None)
    session = opentok.create_session()
    session_id = session.session_id
    doctor_token = session.generate_token()
    patient = patient_info.objects.get(id=patient_id)
    video = video_chat_session.objects.create(Call_from=request.user,Call_for=patient.user, appoinment_id=appoinment,session_id=session_id,user_token=doctor_token)
    video.save()
    return Response({
      "Message":"Call initiated",
      "session_id":session_id,
      "token":doctor_token,
      "id":video.id
    })

class call_doctor_mobile(generics.GenericAPIView):
  serializer_class = video_mobile_serializer

  def post(self, request, *args, **kwargs):
    doctor_id = request.query_params.get('doctor',None)
    appoinment = request.query_params.get('app_id',None)
    session = opentok.create_session()
    session_id = session.session_id
    patient_token = session.generate_token()
    doctor = doctors_info.objects.get(id=doctor_id)
    video = video_chat_session.objects.create(Call_from=request.user,Call_for=doctor.user, appoinment_id=appoinment,session_id=session_id,user_token=patient_token)
    video.save()
    return Response({
      "Message":"Call initiated",
      "session_id":session_id,
      "token":patient_token,
      "id":video.id
    })

class MobAnswerCallAPI(generics.GenericAPIView):
  serializer_class = video_mobile_serializer
  
  def post(self, request, *args, **kwargs):
    session_id = request.query_params.get('id',None)
    video = video_chat_session.objects.get(id=session_id)
    if video.Call_for == request.user:
      video.is_answered = True
      video.save()
      token = opentok.generate_token(video.session_id)
      return Response({
        "Message":"Call Answered",
        "token":token
      })
    return Response(status=status.HTTP_400_BAD_REQUEST)
