from .serializers import specialist_typeSerializer
from .models import specialist_type
from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response


class specialist_typeViewSet(viewsets.ModelViewSet):
    queryset = specialist_type.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = specialist_typeSerializer

class dactivate_Specialist(generics.UpdateAPIView):
    queryset = specialist_type.objects.all()
    serializer_class = specialist_typeSerializer
    permissions = [
        permissions.AllowAny
    ]