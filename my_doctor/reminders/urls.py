from .api import reminders_api, myreminders
from rest_framework import routers
from django.urls import path, include



router = routers.DefaultRouter()
router.register('reminders', reminders_api, 'reminderList')
router.register('myreminders', myreminders, 'myreminders')

urlpatterns = [
    path('',include(router.urls)),
]