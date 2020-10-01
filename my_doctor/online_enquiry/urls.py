from rest_framework import routers
from .api import online_enquiryAPI

router = routers.DefaultRouter()

router.register('onlineEnquiry',online_enquiryAPI,'onlineEnquiry')

urlpatterns=router.urls