from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import os
from django.core.files.storage import default_storage

from paginausuario.models import DatosPersonales

class Command(BaseCommand):
    help = 'Descargar una imagen desde una URL y asignarla como foto_perfil a un perfil (activo por defecto)'

    def add_arguments(self, parser):
        parser.add_argument('--url', required=True, help='URL de la imagen a descargar')
        parser.add_argument('--id', type=int, help='ID del perfil (idperfil). Si se omite se usa el perfil activo (perfilactivo=1)')

    def handle(self, *args, **options):
        url = options.get('url')
        profile_id = options.get('id')

        # Validar URL básica
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            raise CommandError('URL inválida')

        # Seleccionar perfil
        if profile_id:
            perfil = DatosPersonales.objects.filter(idperfil=profile_id).first()
            if not perfil:
                raise CommandError(f'No se encontró perfil con id {profile_id}')
        else:
            perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
            if not perfil:
                raise CommandError('No hay perfil activo (perfilactivo=1) y no se indicó --id')

        self.stdout.write(f'Descargando imagen desde: {url}')
        try:
            # Some servers block default user-agent; set a simple one
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req, timeout=15) as resp:
                content = resp.read()
                ct = resp.headers.get('Content-Type', '')
        except HTTPError as e:
            raise CommandError(f'HTTP error al descargar la imagen: {e.code} {e.reason}')
        except URLError as e:
            raise CommandError(f'Error de URL al descargar la imagen: {e.reason}')
        except Exception as e:
            raise CommandError(f'Error al descargar la imagen: {e}')

        if not content:
            raise CommandError('La descarga no devolvió contenido')

        # Definir nombre de archivo seguro
        ext = 'jpg'
        if 'png' in ct.lower():
            ext = 'png'
        elif 'jpeg' in ct.lower() or 'jpg' in ct.lower():
            ext = 'jpg'
        else:
            # Try to infer from URL path
            path = parsed.path
            _, file_ext = os.path.splitext(path)
            if file_ext.lower() in ['.png', '.jpg', '.jpeg']:
                ext = file_ext.lower().lstrip('.')

        filename = f'from_url_profile_{perfil.idperfil}.{ext}'

        # Guardar en campo foto_perfil usando ContentFile
        try:
            perfil.foto_perfil.save(filename, ContentFile(content), save=True)
            self.stdout.write(self.style.SUCCESS(f'Imagen asignada a perfil {perfil} -> {perfil.foto_perfil.url}'))
        except Exception as e:
            raise CommandError(f'Error al guardar la imagen en el perfil: {e}')
