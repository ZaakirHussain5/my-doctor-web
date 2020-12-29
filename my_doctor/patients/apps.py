from django.apps import AppConfig


class PatientsConfig(AppConfig):
    name = 'patients'

    def ready(self):
        from schedules import scheduler
        scheduler.plan_call()