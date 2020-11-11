from rest_framework import routers
from .api import (NewAppointmentAPI, getDoctorAppointments,appointmentViewSet,
    getPatientAppointments,getAllAppointments, getAppoinmentHistory, getUpcomingAppoinment
)

router = routers.DefaultRouter()
router.register('appointments', appointmentViewSet, 'appointments')
router.register('getPatientsAppointments', getPatientAppointments, 'getPatientsAppointments')
router.register('getAllAppoitnements',getAllAppointments,'getAllAppoitnements')
router.register('getDoctorAppointments', getDoctorAppointments, 'getDoctorAppointments')
router.register('NewAppointment',NewAppointmentAPI,'NewAppointment')
router.register('getAppoinmentHistory', getAppoinmentHistory , 'getAppoinmentHistory')
router.register('getUpcomingAppoinment', getUpcomingAppoinment , 'Patinet_getUpcomingAppoinment')

urlpatterns = router.urls
