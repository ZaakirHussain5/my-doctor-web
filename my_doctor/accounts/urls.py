from rest_framework import routers
from knox.views import LogoutAllView
from .api import fcmTokenAPI,userViewSet,RegisterAPI,LoginAPI,UserAPI, g_loginView, checkEmail
from django.urls import path

router = routers.DefaultRouter()
router.register('user', userViewSet, 'user')
router.register('duplicationCheck', checkEmail, 'duplicationCheck')

urlpatterns = router.urls

urlpatterns.append(path('auth/register',RegisterAPI.as_view(),name='register'))
urlpatterns.append(path('auth/login',LoginAPI.as_view(),name='login'))
urlpatterns.append(path('auth/user',UserAPI.as_view(),name='user'))
urlpatterns.append(path('auth/logout',LogoutAllView.as_view(),name='logout'))
urlpatterns.append(path('fcm_token',fcmTokenAPI.as_view(),name='fdm_token'))
urlpatterns.append(path('g/auth/login',g_loginView.as_view(),name='logout'))

