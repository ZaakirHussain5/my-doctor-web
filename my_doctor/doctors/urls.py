from rest_framework import routers
from .api import doctors_infoViewSet

router = routers.DefaultRouter()
router.register('doctors_info', doctors_infoViewSet, 'doctors_info')

urlpatterns = router.urls
