from .serializers import specialist_typeSerializer
from .models import specialist_type
from rest_framework import viewsets, permissions


class specialist_typeViewSet(viewsets.ModelViewSet):
    queryset = specialist_type.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = specialist_typeSerializer