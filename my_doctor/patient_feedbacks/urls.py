from rest_framework import routers
from .api import patient_feedbacksViewSet

router = routers.DefaultRouter()
router.register('patient_feedbacks', patient_feedbacksViewSet, 'patient_feedbacks')

urlpatterns = router.urls