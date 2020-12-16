from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    name = 'appointment'

    def ready(self):
        import appointment.signals
        from schedules import scheduler
        scheduler.start()
        scheduler.every_15mins_call()
        scheduler.every_10mins_call()
        scheduler.every_5mins_call()
