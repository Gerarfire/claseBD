from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginausuario.urls')),
]

# Servir archivos MEDIA en desarrollo, y opcionalmente en despliegues controlados
# si se establece la variable de entorno SERVE_MEDIA=1 (no recomendado en prod).
if settings.DEBUG or os.environ.get('SERVE_MEDIA', '').lower() in ('1', 'true', 'yes'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)