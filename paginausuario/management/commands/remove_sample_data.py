from django.core.management.base import BaseCommand
from paginausuario.models import DatosPersonales

class Command(BaseCommand):
    help = 'Remove the sample profile and related sample data (Ejemplo Usuario)'

    def handle(self, *args, **options):
        try:
            perfil = DatosPersonales.objects.filter(nombres='Ejemplo', apellidos='Usuario').first()
            if perfil:
                nombre = f"{perfil.nombres} {perfil.apellidos} (id {perfil.idperfil})"
                perfil.delete()
                self.stdout.write(self.style.SUCCESS(f'Sample profile {nombre} and related data deleted.'))
            else:
                self.stdout.write(self.style.WARNING('No sample profile found (nombres=Ejemplo, apellidos=Usuario).'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error deleting sample data: {e}'))
