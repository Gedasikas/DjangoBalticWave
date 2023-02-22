from django.apps import AppConfig

class BalticwaveConfig(AppConfig):
    name = 'balticwave'
    def ready(self):
        from .signals import create_profile, save_profile