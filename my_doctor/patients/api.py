from .serializers import patient_infoSerializer,PatientResgistrationSerializer
from .models import patient_info
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