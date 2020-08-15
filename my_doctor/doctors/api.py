from .serializers import doctors_infoSerializer
from .models import doctors_info
from rest_framework import viewsets, permissions


class doctors_infoViewSet(viewsets.ModelViewSet):
    queryset = doctors_info.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = doctors_infoSerializer