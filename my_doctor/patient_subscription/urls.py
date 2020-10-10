from rest_framework import routers
from .api import MySubscriptionPlans

router = routers.DefaultRouter()
router.register('MySubscriptionPlans', MySubscriptionPlans, 'MySubscriptionPlans')

urlpatterns = router.urls