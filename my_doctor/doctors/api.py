from .serializers import UpdateProfile, doctors_infoSerializer,DoctorRegistration,DoctorTimingsSerializer,AvlDoctorsListSerializer
from .models import doctors_info,DoctorTimings
from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response
from accounts.serializers import UserAuthSerializer
from django.core.exceptions import ObjectDoesNotExist
from knox.models import AuthToken

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

class DoctorTimingsAPI(viewsets.ModelViewSet):
    permissions = [
        permissions.IsAuthenticated
    ]
    serializer_class = DoctorTimingsSerializer

    def get_queryset(self):
      return DoctorTimings.objects.filter(doctor__user=self.request.user)

    def perform_create(self, serializer):
      try:
         DoctorTimings.objects.get(doctor__user=self.request.user).delete()
      except ObjectDoesNotExist:
         pass
      serializer.save()

class DoctorUpdateProfileAPI(generics.GenericAPIView):
    serializer_class = UpdateProfile

    permission_classes=[
        permissions.IsAuthenticated
    ]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(loggedInuser=self.request.user.id)
        print(user)
        return Response({
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class GetLoggedDoctor(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = doctors_infoSerializer

  def get_object(self):
        try:
            doctor = doctors_info.objects.get(user__id=self.request.user.id)
            return doctor
        except ObjectDoesNotExist:
            return Response({
                "Message":"User Not Found"
            },status=404)

class getAvailableDoctors(viewsets.ModelViewSet):
  serializer_class = AvlDoctorsListSerializer
  def get_queryset(self):
    day = self.request.query_params.get('day', None)
    spl = self.request.query_params.get('spl', None)
    queryset = doctors_info.objects.all()
    print(day,spl)
    if spl is not None:
       queryset = doctors_info.objects.filter(specialist_type=spl)
    if day is not None:
       if day=='mon':
          queryset = DoctorTimings.objects.filter(mon=True).filter(doctor__in=queryset)
       if day=='tue':
          queryset = DoctorTimings.objects.filter(tue=True).filter(doctor__in=queryset)
       if day=='wed':
          queryset = DoctorTimings.objects.filter(wed=True).filter(doctor__in=queryset)
       if day=='thu':
          queryset = DoctorTimings.objects.filter(thu=True).filter(doctor__in=queryset)
       if day=='fri':
          queryset = DoctorTimings.objects.filter(fri=True).filter(doctor__in=queryset)
       if day=='sat':
          queryset = DoctorTimings.objects.filter(sat=True).filter(doctor__in=queryset)
       if day=='sun':
          queryset = DoctorTimings.objects.filter(sun=True).filter(doctor__in=queryset)
    return queryset

class DoctorLogout(generics.GenericAPIView):
   def post(self,request):
      if request.user is not None:
         doctor = doctors_info.objects.get(user=request.user).update(is_loggedin=False)
         doctor.save()
         return Response({})
