import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_hojadevida1.settings')
django.setup()
from paginausuario.models import DatosPersonales, VentaGarage
p = DatosPersonales.objects.first()
print('Perfil foto name:', repr(p.foto_perfil.name))
print('Perfil foto url:', getattr(p.foto_perfil, 'url', 'no-url'))
v = VentaGarage.objects.first()
print('Venta imagen name:', repr(v.imagen.name))
print('Venta imagen url:', getattr(v.imagen, 'url', 'no-url'))
