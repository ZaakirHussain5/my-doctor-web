from rest_framework import routers
from .api import patient_wallet_detailsViewSet

router = routers.DefaultRouter()
router.register('patient_wallet_details', patient_wallet_detailsViewSet, 'patient_wallet_details')

urlpatterns = router.urls