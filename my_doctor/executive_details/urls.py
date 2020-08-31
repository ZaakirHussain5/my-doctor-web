from rest_framework import routers
from .api import executive_detailsViewSet,ExecutiveRegistrationAPI
from django.urls import path,include

router = routers.DefaultRouter()
router.register('executive_details', executive_detailsViewSet, 'executive_details')

urlpatterns = [
    path('',include(router.urls)),
    path('executiveRegistration',ExecutiveRegistrationAPI.as_view(),name='executiveRegistration')
]