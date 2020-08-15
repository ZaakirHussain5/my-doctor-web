from rest_framework import routers
from .api import subscription_plansViewSet

router = routers.DefaultRouter()
router.register('subscription_plans', subscription_plansViewSet, 'subscription_plans')

urlpatterns = router.urls
