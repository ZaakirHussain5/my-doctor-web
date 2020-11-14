from rest_framework import routers
from .api import (NewAppointmentAPI, getDoctorAppointments,appointmentViewSet,
    getPatientAppointments,getAllAppointments, getAppoinmentHistory, getUpcomingAppoinment, upComingAppoinment,
    todaysAppoinment, previousAppoinment
)

router = routers.DefaultRouter()
router.register('appointments', appointmentViewSet, 'appointments')
router.register('getPatientsAppointments', getPatientAppointments, 'getPatientsAppointments')
router.register('getAllAppoitnements',getAllAppointments,'getAllAppoitnements')
router.register('getDoctorAppointments', getDoctorAppointments, 'getDoctorAppointments')
router.register('NewAppointment',NewAppointmentAPI,'NewAppointment')
router.register('getAppoinmentHistory', getAppoinmentHistory , 'getAppoinmentHistory')
router.register('getUpcomingAppoinment', getUpcomingAppoinment , 'Patinet_getUpcomingAppoinment')
router.register('upComingAppoinment', upComingAppoinment,'upComingAppoinment')
router.register('todaysAppoinment', todaysAppoinment,'todaysAppoinment')
router.register('previousAppoinment', previousAppoinment,'previousAppoinment')

urlpatterns = router.urls
