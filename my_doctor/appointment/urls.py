from rest_framework import routers
from .api import getDoctorAppointments,appointmentViewSet,getPatientAppointments,getAllAppointments

router = routers.DefaultRouter()
router.register('appointments', appointmentViewSet, 'appointments')
router.register('getPatientsAppointments', getPatientAppointments, 'getPatientsAppointments')
router.register('getAllAppoitnements',getAllAppointments,'getAllAppoitnements')
router.register('getDoctorAppointments', getDoctorAppointments, 'getDoctorAppointments')

urlpatterns = router.urls
