from rest_framework import routers
from .api import transactionsViewSet

router = routers.DefaultRouter()
router.register('transactions', transactionsViewSet, 'transactions')

urlpatterns = router.urls