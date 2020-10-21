from .api import vedioChatOparetion
from rest_framework import routers
from django.urls import path, include



router = routers.DefaultRouter()
router.register('vedioChatOparetion', vedioChatOparetion, 'vedioChatOparetion')

urlpatterns = [
    path('',include(router.urls)),
]