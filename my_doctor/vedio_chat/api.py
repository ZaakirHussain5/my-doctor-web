from rest_framework import permissions,viewsets, mixins,generics
from rest_framework.response import Response
from .models import VedioChat
from .serializers import VedioChatSerializer
from doctors.models import doctors_info
from opentok import OpenTok,MediaModes
opentok = OpenTok("46964534", "76ca83ec02f7c0ef904f536a2d0bc251df25d8a4")

class vedioChatOparetion(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = VedioChatSerializer

    def get_queryset(self):
        queryset = VedioChat.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = self.request.user.call_for.all()
        return queryset
    
    def perform_create(self,serializer):
        return serializer.save()

class InitiateCallAPI(generics.GenericAPIView):
  serializer_class = VedioChatSerializer

  def post(self, request, *args, **kwargs):
    doctor_id = self.request.query_params.get('doctor_id',None)
    session = opentok.create_session(media_mode=MediaModes.routed)
    session_id = session.session_id
    token = session.generate_token()
    doctor = doctors_info.objects.get(id=doctor_id)
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save(Call_from=self.request.user,Call_for = doctor.user,Call_session=session_id)
    return Response({
      "session_id": session_id,
      "token": token
    })




