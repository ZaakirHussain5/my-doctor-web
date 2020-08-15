from rest_framework import routers
from .api import patient_health_infoViewSet

router = routers.DefaultRouter()
router.register('patient_health_info', patient_health_infoViewSet, 'patient_health_info')

urlpatterns = router.urls
