from rest_framework import routers
from .api import appointmentViewSet,getPatientAppointments

router = routers.DefaultRouter()
router.register('appointments', appointmentViewSet, 'appointment')
router.register('getPatientsAppointments', getPatientAppointments, 'getPatientsAppointments')

urlpatterns = router.urls
