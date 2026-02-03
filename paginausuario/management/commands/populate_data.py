from django.core.management.base import BaseCommand
from paginausuario.models import DatosPersonales, ExperienciaLaboral, Reconocimiento, CursoRealizado, ProductoAcademico, ProductoLaboral, VentaGarage
from datetime import date
from django.core.files.base import ContentFile
import base64

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

        # Añadir imagen de ejemplo al perfil si no existe (imagen de placeholder más visible)
        if not perfil.foto_perfil:
            try:
                from urllib.request import urlopen
                url = 'https://via.placeholder.com/240x240.png?text=Perfil'
                resp = urlopen(url, timeout=5)
                data = resp.read()
                perfil.foto_perfil.save('sample_perfil.png', ContentFile(data), save=True)
                self.stdout.write(self.style.SUCCESS('Imagen de perfil de ejemplo añadida (descargada)'))
            except Exception:
                # Fallback a 1x1 si no hay red
                sample_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="
                image_data = base64.b64decode(sample_b64)
                perfil.foto_perfil.save('sample_perfil.png', ContentFile(image_data), save=True)
                self.stdout.write(self.style.SUCCESS('Imagen de perfil de ejemplo añadida (fallback)'))

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
        rec = Reconocimiento.objects.filter(
            idperfilconqueestaactivo=perfil,
            tiporeconocimiento='Académico'
        ).first()
        
        if not rec:
            rec = Reconocimiento.objects.create(
                idperfilconqueestaactivo=perfil,
                tiporeconocimiento='Académico',
                fechareconocimiento=date(2022, 6, 15),
                descripcionreconocimiento='Mejor Proyecto de Fin de Carrera',
                entidadpatrocinadora='Universidad Central del Ecuador',
                activarparaqueseveaenfront=True
            )
            self.stdout.write(self.style.SUCCESS('Reconocimiento creado'))
        else:
            self.stdout.write('Reconocimiento ya existe')

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
            # Añadir imagen de ejemplo a la venta si no existe (placeholder)
            if not venta.imagen:
                try:
                    from urllib.request import urlopen
                    url = 'https://via.placeholder.com/320x240.png?text=Venta'
                    resp = urlopen(url, timeout=5)
                    data = resp.read()
                    venta.imagen.save('sample_venta.png', ContentFile(data), save=True)
                    self.stdout.write(self.style.SUCCESS('Imagen de venta de ejemplo añadida (descargada)'))
                except Exception:
                    sample_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="
                    image_data = base64.b64decode(sample_b64)
                    venta.imagen.save('sample_venta.png', ContentFile(image_data), save=True)
                    self.stdout.write(self.style.SUCCESS('Imagen de venta de ejemplo añadida (fallback)'))

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados exitosamente'))