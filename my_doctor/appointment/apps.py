from django.apps import AppConfig


class AppointmentConfig(AppConfig):
    name = 'appointment'

    def ready(self):
        from schedules import scheduler
        scheduler.start()
        scheduler.every_15mins_call()