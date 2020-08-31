from rest_framework import routers
from .api import doctor_paymentsViewSet

router = routers.DefaultRouter()
router.register('doctor_payments', doctor_paymentsViewSet, 'doctor_payments')

urlpatterns = router.urls