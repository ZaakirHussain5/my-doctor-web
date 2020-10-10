from rest_framework.routers import DefaultRouter
from .api import billPaymentsRecord

router = DefaultRouter()
router.register('CheckBillPayments', billPaymentsRecord, 'billpayments')

urlpatterns = router.urls
