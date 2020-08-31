from .serializers import doctors_infoSerializer,DoctorRegistration
from .models import doctors_info
from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response
from accounts.serializers import UserAuthSerializer


class doctors_infoViewSet(viewsets.ModelViewSet):
    queryset = doctors_info.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = doctors_infoSerializer

class DoctorRegisterAPI(generics.GenericAPIView):
  serializer_class = DoctorRegistration

  def get_queryset(self):
    return doctors_info.objects.all()

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "Doctor": UserAuthSerializer(user, context=self.get_serializer_context()).data
    })