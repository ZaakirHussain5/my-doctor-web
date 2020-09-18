from rest_framework import routers
from .api import consultationsViewSet,getAllConsultations,getPatientConsultations

router = routers.DefaultRouter()
router.register('consultations', consultationsViewSet, 'consultations')
router.register('getAllConsultations', getAllConsultations, 'getAllConsultations')
router.register('getPatientConsultations', getPatientConsultations, 'getPatientConsultations')

urlpatterns = router.urls