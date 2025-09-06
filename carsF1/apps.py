from django.apps import AppConfig


class Carsf1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carsF1'

    def ready(self):
        import carsF1.signals
        