from rest_framework import viewsets
from .models import promo_code
from .serializers import promo_codeSerializer
from rest_framework import permissions


class promocode_work(viewsets.ModelViewSet):
    serializer_class = promo_codeSerializer
    permissions = [
        permissions.AllowAny
    ]

    queryset = promo_code.objects.all()
