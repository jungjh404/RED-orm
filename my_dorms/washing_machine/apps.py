from django.apps import AppConfig
from django.conf import settings

class WashingMachineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'washing_machine'

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import scheduler
            scheduler.start()
