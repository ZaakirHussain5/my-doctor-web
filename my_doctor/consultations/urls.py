from rest_framework import routers
from .api import consultationsViewSet

router = routers.DefaultRouter()
router.register('consultations', consultationsViewSet, 'consultations')

urlpatterns = router.urls