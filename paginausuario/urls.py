"""
URL configuration for paginausuario app.
"""
from django.urls import path
from . import views

app_name = 'paginausuario'

urlpatterns = [
    path('', views.hoja_vida, name='hoja_vida'),
    path('experiencias/', views.experiencias, name='experiencias'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('cursos/', views.cursos, name='cursos'),
    path('productos-academicos/', views.productos_academicos, name='productos_academicos'),
    path('productos-laborales/', views.productos_laborales, name='productos_laborales'),
    path('ventas-garage/', views.ventas_garage, name='ventas_garage'),
    path('experiencias/pdf/', views.experiencias_pdf, name='experiencias_pdf'),
    path('reconocimientos/pdf/', views.reconocimientos_pdf, name='reconocimientos_pdf'),
    path('cursos/pdf/', views.cursos_pdf, name='cursos_pdf'),
    path('productos-academicos/pdf/', views.productos_academicos_pdf, name='productos_academicos_pdf'),
    path('productos-laborales/pdf/', views.productos_laborales_pdf, name='productos_laborales_pdf'),
    path('ventas-garage/pdf/', views.ventas_garage_pdf, name='ventas_garage_pdf'),
    path('hoja_vida/pdf/', views.hoja_vida_pdf, name='hoja_vida_pdf'),
    path('create_superuser/', views.create_superuser),
]
from paginausuario import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hoja_vida, name='hoja_vida'),  # Página principal con perfil y menú
    path('experiencias/', views.experiencias, name='experiencias'),
    path('reconocimientos/', views.reconocimientos, name='reconocimientos'),
    path('cursos/', views.cursos, name='cursos'),
    path('productos-academicos/', views.productos_academicos, name='productos_academicos'),
    path('productos-laborales/', views.productos_laborales, name='productos_laborales'),
    path('ventas-garage/', views.ventas_garage, name='ventas_garage'),
    path('experiencias/pdf/', views.experiencias_pdf, name='experiencias_pdf'),
    path('reconocimientos/pdf/', views.reconocimientos_pdf, name='reconocimientos_pdf'),
    path('cursos/pdf/', views.cursos_pdf, name='cursos_pdf'),
    path('productos-academicos/pdf/', views.productos_academicos_pdf, name='productos_academicos_pdf'),
    path('productos-laborales/pdf/', views.productos_laborales_pdf, name='productos_laborales_pdf'),
    path('ventas-garage/pdf/', views.ventas_garage_pdf, name='ventas_garage_pdf'),
    path('hoja_vida/pdf/', views.hoja_vida_pdf, name='hoja_vida_pdf'),
    path('create_superuser/', views.create_superuser),
    path('', include('paginausuario.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include