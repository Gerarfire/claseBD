"""
URL configuration for django_hojadevida1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from paginausuario import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hoja_vida, name='hoja_vida'),  # Página principal con perfil y menú
    path('experiencias/', views.experiencias, name='experiencias'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('cursos/', views.cursos, name='cursos'),
    path('productos-academicos/', views.productos_academicos, name='productos_academicos'),
    path('productos-laborales/', views.productos_laborales, name='productos_laborales'),
    path('hoja_vida/pdf/', views.hoja_vida_pdf, name='hoja_vida_pdf'),
    path('create_superuser/', views.create_superuser),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
