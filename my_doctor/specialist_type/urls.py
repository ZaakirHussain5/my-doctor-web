from rest_framework import routers
from .api import specialist_typeViewSet

router = routers.DefaultRouter()
router.register('specialist_types', specialist_typeViewSet, 'specialist_type')

urlpatterns = router.urls
