from rest_framework import routers
from .api import promocode_work

router = routers.DefaultRouter()
router.register('promocode_work', promocode_work, 'promocode_work')


urlpatterns = router.urls
