from django.apps import AppConfig
from django.db.models import signals
from .signals import user_pre_save


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from .models import User

        signals.pre_save.connect(user_pre_save, sender=User)
