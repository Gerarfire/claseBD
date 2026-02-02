from django.core.management.base import BaseCommand
from paginausuario.models import DatosPersonales

class Command(BaseCommand):
    help = 'Set a given profile active and unset others. Use --id or --username.'

    def add_arguments(self, parser):
        parser.add_argument('--id', type=int, help='ID of the profile (idperfil)')
        parser.add_argument('--username', type=str, help='Match by nombres or apellidos')

    def handle(self, *args, **options):
        pid = options.get('id')
        username = options.get('username')

        if not pid and not username:
            self.stderr.write('Provide --id or --username')
            return

        if pid:
            profile = DatosPersonales.objects.filter(idperfil=pid).first()
        else:
            profile = DatosPersonales.objects.filter(nombres__icontains=username).first()

        if not profile:
            self.stderr.write('Profile not found')
            return

        DatosPersonales.objects.update(perfilactivo=0)
        profile.perfilactivo = 1
        profile.save()
        self.stdout.write(self.style.SUCCESS(f'Profile {profile} set active.'))