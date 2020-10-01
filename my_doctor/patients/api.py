from .serializers import UpdateProfile,patient_infoSerializer,PatientResgistrationSerializer,medical_historySerializer,groupsSerializer,PatientResgistrationApp
from .models import patient_info,medical_history,groups
from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response
from accounts.serializers import UserAuthSerializer
from django.core.exceptions import ObjectDoesNotExist
from knox.models import AuthToken

class patient_infoViewSet(viewsets.ModelViewSet):
    queryset = patient_info.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = patient_infoSerializer

class PatientResgistrationAPI(generics.GenericAPIView):
    serializer_class = PatientResgistrationSerializer
    
    def get_queryset(self):
        return patient_info.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data
        })

class PatientResgistrationAppAPI(generics.GenericAPIView):
    serializer_class = PatientResgistrationApp
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class PatientUpdateProfileAPI(generics.GenericAPIView):
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

class GetLoggedPatient(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = patient_infoSerializer

  def get_object(self):
        try:
            patient = patient_info.objects.get(user__id=self.request.user.id)
            return patient
        except ObjectDoesNotExist:
            return Response({
                "Message":"User Not Found"
            },status=404)

class medical_historyViewSet(viewsets.ModelViewSet):
    queryset = medical_history.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = medical_historySerializer

class groupsViewSet(viewsets.ModelViewSet):
    queryset = groups.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = groupsSerializer