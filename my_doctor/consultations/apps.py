from django.apps import AppConfig


class ConsultationsConfig(AppConfig):
    name = 'consultations'

    def ready(self):
        import consultations.signals