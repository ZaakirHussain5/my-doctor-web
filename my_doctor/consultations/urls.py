from rest_framework import routers
from .api import consultationsViewSet,getAllConsultations

router = routers.DefaultRouter()
router.register('consultations', consultationsViewSet, 'consultations')
router.register('getAllConsultations', getAllConsultations, 'getAllConsultations')

urlpatterns = router.urls