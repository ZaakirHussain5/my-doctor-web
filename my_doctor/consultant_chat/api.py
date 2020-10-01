from .serializers import consultant_chatSerializer
from .models import consultant_chat
from rest_framework import viewsets, permissions


class consultant_chatViewSet(viewsets.ModelViewSet):
    
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = consultant_chatSerializer

    def get_queryset(self):
        queryset = consultant_chat.objects.all()
        cons_id = self.request.query_params.get('cons_id', None)
        if cons_id is not None:
            queryset = consultant_chat.objects.filter(consultation_id=cons_id)
            return queryset
        return consultant_chat.objects.all()