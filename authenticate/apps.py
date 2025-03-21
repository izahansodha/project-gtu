from django.apps import AppConfig


class AuthenticateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticate'

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticate'

    def ready(self):
        import authenticate.singnal # Ensure signals are loaded
