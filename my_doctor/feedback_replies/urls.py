from rest_framework import routers
from .api import feedback_repliesViewSet

router = routers.DefaultRouter()
router.register('feedback_replies', feedback_repliesViewSet, 'feedback_replies')

urlpatterns = router.urls