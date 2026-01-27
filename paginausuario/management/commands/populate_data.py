from django.core.management.base import BaseCommand
from paginausuario.models import DatosPersonales, ExperienciaLaboral, Reconocimiento, CursoRealizado, ProductoAcademico, ProductoLaboral, VentaGarage
from datetime import date

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Crear perfil principal si no existe
        perfil, created = DatosPersonales.objects.get_or_create(
            idperfil=1,
            defaults={
                'descripcionperfil': 'Profesional en desarrollo de software y gestión de proyectos',
                'perfilactivo': 1,
                'apellidos': 'Usuario',
                'nombres': 'Ejemplo',
                'nacionalidad': 'Ecuatoriana',
                'lugarnacimiento': 'Quito',
                'fechanacimiento': date(1990, 5, 15),
                'numerocedula': '1234567890',
                'sexo': 'H',
                'estadocivil': 'Soltero',
                'licenciaconducir': 'B1',
                'telefonoconvencional': '0991234567',
                'telefonofijo': '022345678',
                'direcciontrabajo': 'Av. Principal 123',
                'direcciondomiciliaria': 'Calle Secundaria 456',
                'sitioweb': 'https://miportafolio.com'
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Perfil principal creado'))
        else:
            self.stdout.write('Perfil principal ya existe')

        # Crear experiencia laboral de ejemplo
        exp, created = ExperienciaLaboral.objects.get_or_create(
            idperfilconqueestaactivo=perfil,
            cargodesempenado='Desarrollador Full Stack',
            defaults={
                'nombrempresa': 'Tech Solutions S.A.',
                'lugarempresa': 'Quito, Ecuador',
                'fechainiciogestion': date(2020, 1, 1),
                'fechafingestion': date(2023, 12, 31),
                'descripcionfunciones': 'Desarrollo de aplicaciones web, mantenimiento de sistemas, gestión de proyectos.',
                'activarparaqueseveaenfront': True
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Experiencia laboral creada'))

        # Crear reconocimiento de ejemplo
        rec, created = Reconocimiento.objects.get_or_create(
            idperfilconqueestaactivo=perfil,
            tiporeconocimiento='Académico',
            defaults={
                'fechareconocimiento': date(2022, 6, 15),
                'descripcionreconocimiento': 'Mejor Proyecto de Fin de Carrera',
                'entidadpatrocinadora': 'Universidad Central del Ecuador',
                'activarparaqueseveaenfront': True
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Reconocimiento creado'))

        # Crear curso de ejemplo
        curso, created = CursoRealizado.objects.get_or_create(
            idperfilconqueestaactivo=perfil,
            nombrecurso='Desarrollo Web con Django',
            defaults={
                'fechainicio': date(2023, 3, 1),
                'fechafin': date(2023, 6, 30),
                'totalhoras': 120,
                'descripcioncurso': 'Curso completo de desarrollo web con Django Framework',
                'entidadpatrocinadora': 'Platzi',
                'activarparaqueseveaenfront': True
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Curso creado'))

        # Crear producto académico de ejemplo
        prod_acad, created = ProductoAcademico.objects.get_or_create(
            idperfilconqueestaactivo=perfil,
            nombrerecurso='Sistema de Gestión Académica',
            defaults={
                'clasificador': 'Proyecto de Investigación',
                'descripcion': 'Sistema web para gestión de estudiantes y calificaciones',
                'activarparaqueseveaenfront': True
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Producto académico creado'))

        # Crear producto laboral de ejemplo
        prod_lab, created = ProductoLaboral.objects.get_or_create(
            idperfilconqueestaactivo=perfil,
            nombreproducto='Aplicación Móvil de Delivery',
            defaults={
                'fechaproducto': date(2023, 8, 20),
                'descripcion': 'App móvil para pedidos de comida a domicilio',
                'activarparaqueseveaenfront': True
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Producto laboral creado'))

        # Crear venta de garage de ejemplo
        venta, created = VentaGarage.objects.get_or_create(
            idperfilconqueestaactivo=perfil,
            nombreproducto='Bicicleta Montañera',
            defaults={
                'estadoproducto': 'Bueno',
                'descripcion': 'Bicicleta Specialized Stumpjumper en excelente estado',
                'valordelbien': 850.50,
                'activarparaqueseveaenfront': True
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Venta de garage creada'))

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados exitosamente'))