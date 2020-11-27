from rest_framework import routers
from .api import doctor_paymentsViewSet, doctor_listViewset, doctor_dataView

router = routers.DefaultRouter()
router.register('doctor_payments', doctor_paymentsViewSet, 'doctor_payments')
router.register('doctor_paymentlist', doctor_listViewset, 'doctor_paymentlist')
router.register('doctor_dataView', doctor_dataView, 'doctor_dataView')

urlpatterns = router.urls