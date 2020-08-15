from rest_framework import routers
from .api import userViewSet,RegisterAPI,LoginAPI,UserAPI
from django.urls import path

router = routers.DefaultRouter()
router.register('user', userViewSet, 'user')

urlpatterns = router.urls

urlpatterns.append(path('auth/register',RegisterAPI.as_view(),name='register'))
urlpatterns.append(path('auth/login',LoginAPI.as_view(),name='login'))
urlpatterns.append(path('auth/user',UserAPI.as_view(),name='user'))

