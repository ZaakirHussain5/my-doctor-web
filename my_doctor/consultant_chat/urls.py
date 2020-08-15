from rest_framework import routers
from .api import consultant_chatViewSet

router = routers.DefaultRouter()
router.register('consultant_chats', consultant_chatViewSet, 'consultant_chat')

urlpatterns = router.urls