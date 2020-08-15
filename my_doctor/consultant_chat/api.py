from .serializers import consultant_chatSerializer
from .models import consultant_chat
from rest_framework import viewsets, permissions


class consultant_chatViewSet(viewsets.ModelViewSet):
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = consultant_chatSerializer

    def get_queryset(self):
        return self.request.user.cons_chats.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)