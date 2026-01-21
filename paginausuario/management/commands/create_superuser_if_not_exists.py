from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Crea un superusuario si no existe'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Nombre de usuario')
        parser.add_argument('--email', type=str, help='Email')
        parser.add_argument('--password', type=str, help='Contraseña')

    def handle(self, *args, **options):
        username = options['username'] or 'admin'
        email = options['email'] or 'admin@example.com'
        password = options['password'] or 'admin123'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" creado exitosamente.'))
        else:
            self.stdout.write(self.style.WARNING(f'El superusuario "{username}" ya existe.'))