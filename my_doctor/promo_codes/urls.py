from rest_framework import routers
from .api import promocode_work, apply_promoCode
from django.urls import path

router = routers.DefaultRouter()
router.register('promocode_work', promocode_work, 'promocode_work')


urlpatterns = router.urls
urlpatterns.append(path('apply_promoCode', apply_promoCode.as_view(), name="applyPromoCode"))