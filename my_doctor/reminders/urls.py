from .api import reminders_api
from rest_framework import routers
from django.urls import path, include



router = routers.DefaultRouter()
router.register('reminderList', reminders_api, 'remindersList')

urlpatterns = [
    path('',include(router.urls)),
]