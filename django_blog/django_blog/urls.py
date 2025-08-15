# django_blog/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # For a simple home page example
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Django's built-in auth URLs (login, logout, password reset, etc.)
    path('accounts/', include('blog.urls')), # Your app's custom user URLs (for register and profile)
    path('', TemplateView.as_view(template_name='index.html'), name='index'), # Simple home page
]

# For serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

