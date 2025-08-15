# blog/apps.py
from django.apps import AppConfig

class BlogConfig(AppConfig): # Renamed to BlogConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog' # App name

    def ready(self):
        import blog.signals # Import signals here to ensure they are loaded