from rest_framework import routers
from .api import specialist_typeViewSet,dactivate_Specialist
from django.urls import path,include

router = routers.DefaultRouter()
router.register('specialist_types', specialist_typeViewSet, 'specialist_type')

urlpatterns =[
    path('',include(router.urls)),
    path('dactivate_Specialist',dactivate_Specialist.as_view())
] 
