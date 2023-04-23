from django.apps import AppConfig

class ViewersCountMiddlewareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'viewers_count'
    verbose_name = 'Viewers Count'

