from rest_framework import routers
from .api import appointmentViewSet,getPatientAppointments,getAllAppointments

router = routers.DefaultRouter()
router.register('appointments', appointmentViewSet, 'appointments')
router.register('getPatientsAppointments', getPatientAppointments, 'getPatientsAppointments')
router.register('getAllAppoitnements',getAllAppointments,'getAllAppoitnements')

urlpatterns = router.urls
