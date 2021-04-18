from rest_framework import routers
from .api import MySubscriptionPlans, allSubscriptionForAdmin,getPlans,subscribeToAPlan
from django.urls import path,include

router = routers.DefaultRouter()
router.register('MySubscriptionPlan', MySubscriptionPlans, 'MySubscriptionPlans')
router.register('allSubscription_plans', allSubscriptionForAdmin, 'allSubscriptionAdmin')

urlpatterns = [
    path('',include(router.urls)),
    path('getPlans',getPlans,name="getPlans"),
    path('plans/subscribe',subscribeToAPlan.as_view(),name="planSubscribe")
]