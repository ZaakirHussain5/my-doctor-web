from rest_framework import permissions,viewsets, mixins,generics
from rest_framework.response import Response
from .models import VedioChat
from .serializers import VedioChatSerializer
from doctors.models import doctors_info
from patients.models import patient_info

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
    video.is_answered = True
    video.save()
    return Response({
      "Message":"Call Answered",
      "id":video.id
    })

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




