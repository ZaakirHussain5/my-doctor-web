from rest_framework import routers
from .api import MySubscriptionPlans, allSubscriptionForAdmin

router = routers.DefaultRouter()
router.register('MySubscriptionPlans', MySubscriptionPlans, 'MySubscriptionPlans')
router.register('allSubscription_plans', allSubscriptionForAdmin, 'allSubscriptionAdmin')

urlpatterns = router.urls