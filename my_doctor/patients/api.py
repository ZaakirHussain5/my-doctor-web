from .serializers import patient_infoSerializer,PatientResgistrationSerializer,medical_historySerializer,groupsSerializer,PatientResgistrationApp
from .models import patient_info,medical_history,groups
from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response
from accounts.serializers import UserAuthSerializer

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
            "Patient": UserAuthSerializer(user, context=self.get_serializer_context()).data
        })

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