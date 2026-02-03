from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

#BD tabla datos_personales
class DatosPersonales(models.Model):
    SEXO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ]

    idperfil = models.AutoField(primary_key=True)
    descripcionperfil = models.CharField(max_length=200)
    perfilactivo = models.IntegerField(default=1)

    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)

    nacionalidad = models.CharField(max_length=20, blank=True, null=True)
    lugarnacimiento = models.CharField(max_length=60, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)

    numerocedula = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        blank=True,
        null=True
    )

    estadocivil = models.CharField(max_length=50, blank=True, null=True)
    licenciaconducir = models.CharField(max_length=6, blank=True, null=True)

    telefonoconvencional = models.CharField(max_length=15, blank=True, null=True)
    telefonofijo = models.CharField(max_length=15, blank=True, null=True)

    direcciontrabajo = models.CharField(max_length=50, blank=True, null=True)
    direcciondomiciliaria = models.CharField(max_length=50, blank=True, null=True)

    sitioweb = models.CharField(max_length=60, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    # Permitir configurar la foto de perfil por URL (uso preferente sobre upload si está presente)
    foto_perfil_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'datospersonales'

    def save(self, *args, **kwargs):
        """Override save to:
        - convert uploaded profile images to JPEG (.jpg) and ensure consistent format.
        - ensure there is only one profile with perfilactivo=1 (set others to 0).
        - if foto_perfil_url is set, we leave the file field untouched (URL takes precedence for display).
        """
        from PIL import Image
        import os
        from django.core.files.base import ContentFile
        from io import BytesIO

        # If a new image file was uploaded, convert it to JPEG
        # NOTE: if foto_perfil_url is present we do not replace it; both can coexist but URL is used in templates
        if self.foto_perfil and not str(self.foto_perfil).lower().endswith('.jpg'):
            try:
                img = Image.open(self.foto_perfil)
                rgb_im = img.convert('RGB')  # convert PNG/others with alpha to RGB
                buffer = BytesIO()
                rgb_im.save(buffer, format='JPEG', quality=90)
                buffer.seek(0)

                # Create a new filename with .jpg extension using only the basename to avoid double folder nesting
                base, _ = os.path.splitext(self.foto_perfil.name)
                filename = os.path.basename(base)
                new_name = f"{filename}.jpg"

                # Replace the file with the converted JPEG (upload_to will add the folder)
                self.foto_perfil.save(new_name, ContentFile(buffer.read()), save=False)
            except Exception:
                # If conversion fails, ignore and keep original file (will still work if it's an image)
                pass

        # If this profile is being set as active, deactivate others first
        try:
            if getattr(self, 'perfilactivo', 0) == 1:
                # exclude self.pk if it exists (for new instances self.pk may be None)
                from django.db import transaction
                with transaction.atomic():
                    from .models import DatosPersonales as _DP
                    _DP.objects.exclude(pk=self.pk).update(perfilactivo=0)
        except Exception:
            # If anything goes wrong, ignore and proceed to save — better to save than to block.
            pass

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    def clean(self):
        today = date.today()
        if self.fechanacimiento and self.fechanacimiento > today:
            raise ValidationError('La fecha de nacimiento no puede ser futura.')

#BD tabla experiencia laboral
class ExperienciaLaboral(models.Model):
    idexperiencialaboral = models.AutoField(primary_key=True)

    idperfilconqueestaactivo = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )

    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50)
    emailempresa = models.CharField(max_length=100, blank=True, null=True)
    sitiowebempresa = models.CharField(max_length=100, blank=True, null=True)
    nombrecontactoempresarial = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoempresarial = models.CharField(max_length=60, blank=True, null=True)
    fechainiciogestion = models.DateField()
    fechafingestion = models.DateField(blank=True, null=True)
    descripcionfunciones = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Activar para que se vea en front")
    rutacertificado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'experiencialaboral'

    def __str__(self):
        return f"{self.cargodesempenado} - {self.nombrempresa}"

    def clean(self):
        today = date.today()
        if self.fechainiciogestion > today:
            raise ValidationError('La fecha de inicio no puede ser futura.')
        if self.fechafingestion and self.fechafingestion > today:
            raise ValidationError('La fecha de fin no puede ser futura.')
        if self.fechafingestion and self.fechafingestion < self.fechainiciogestion:
            raise ValidationError('La fecha de fin no puede ser anterior a la fecha de inicio.')


#BD tabla reconocimientos
class Reconocimiento(models.Model):
    idreconocimiento = models.AutoField(primary_key=True)

    idperfilconqueestaactivo = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )

    TIPO_RECONOCIMIENTO_CHOICES = [
        ('Académico', 'Académico'),
        ('Público', 'Público'),
        ('Privado', 'Privado'),
    ]

    tiporeconocimiento = models.CharField(
        max_length=100,
        choices=TIPO_RECONOCIMIENTO_CHOICES
    )
    fechareconocimiento = models.DateField()
    descripcionreconocimiento = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoauspicia = models.CharField(max_length=60, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Activar para que se vea en front")
    rutacertificado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'reconocimientos'

    def __str__(self):
        return f"{self.tiporeconocimiento} - {self.entidadpatrocinadora}"

    def clean(self):
        today = date.today()
        if self.fechareconocimiento > today:
            raise ValidationError('La fecha del reconocimiento no puede ser futura.')

#BD tabla cursos realizados
class CursoRealizado(models.Model):
    idcursorealizado = models.AutoField(primary_key=True)

    idperfilconqueestaactivo = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )

    nombrecurso = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField(blank=True, null=True)
    totalhoras = models.IntegerField()
    descripcioncurso = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoauspicia = models.CharField(max_length=60, blank=True, null=True)
    emailempresapatrocinadora = models.CharField(max_length=60, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Activar para que se vea en front")
    rutacertificado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'cursosrealizados'

    def __str__(self):
        return f"{self.nombrecurso} ({self.totalhoras} horas)"

    def clean(self):
        today = date.today()
        if self.fechainicio > today:
            raise ValidationError('La fecha de inicio del curso no puede ser futura.')
        if self.fechafin and self.fechafin > today:
            raise ValidationError('La fecha de fin del curso no puede ser futura.')
        if self.fechafin and self.fechafin < self.fechainicio:
            raise ValidationError('La fecha de fin no puede ser anterior a la fecha de inicio.')


#BD tabla productos academicos
class ProductoAcademico(models.Model):
    idproductoacademico = models.AutoField(primary_key=True)

    idperfilconqueestaactivo = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )

    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Activar para que se vea en front")

    class Meta:
        db_table = 'productosacademicos'

    def __str__(self):
        return self.nombrerecurso

 
#BD tabla productos laborales
class ProductoLaboral(models.Model):
    idproductoslaborales = models.AutoField(primary_key=True)

    idperfilconqueestaactivo = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )

    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField()
    descripcion = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Activar para que se vea en front")

    class Meta:
        db_table = 'productoslaborales'

    def __str__(self):
        return self.nombreproducto

    def clean(self):
        today = date.today()
        if self.fechaproducto > today:
            raise ValidationError('La fecha del producto laboral no puede ser futura.')


#BD tabla ventas garage
class VentaGarage(models.Model):
    idventagarage = models.AutoField(primary_key=True)

    idperfilconqueestaactivo = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )

    ESTADO_PRODUCTO_CHOICES = [
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
    ]

    nombreproducto = models.CharField(max_length=100)

    estadoproducto = models.CharField(
        max_length=40,
        choices=ESTADO_PRODUCTO_CHOICES
    )

    descripcion = models.CharField(max_length=100)

    # Nueva imagen opcional para la venta de garage
    imagen = models.ImageField(upload_to='ventas_garage/', blank=True, null=True)
    # Soporte por URL para imágenes (permite enseñar imágenes de la web sin subir archivo)
    imagen_url = models.URLField(blank=True, null=True)

    valordelbien = models.DecimalField(max_digits=5, decimal_places=2)

    activarparaqueseveaenfront = models.BooleanField(default=True, verbose_name="Activar para que se vea en front")

    class Meta:
        db_table = 'ventagarage'

    def __str__(self):
        return f"{self.nombreproducto} - {self.estadoproducto}"

    def clean(self):
        from django.core.exceptions import ValidationError
        # Validate imagen file if present
        if self.imagen:
            try:
                file = self.imagen
                max_size = 5 * 1024 * 1024
                if hasattr(file, 'size') and file.size > max_size:
                    raise ValidationError('La imagen es demasiado grande (máx 5 MB).')
                from PIL import Image
                file.seek(0)
                img = Image.open(file)
                fmt = (img.format or '').upper()
                if fmt not in ('JPEG', 'PNG'):
                    raise ValidationError('Formato de imagen no soportado. Use JPEG o PNG.')
                max_dim = 4000
                if img.width > max_dim or img.height > max_dim:
                    raise ValidationError('Dimensiones demasiado grandes (máx 4000x4000).')
            except ValidationError:
                raise
            except Exception:
                raise ValidationError('No se pudo procesar la imagen.')

        # Validate imagen_url if present: must be reachable and point to an image
        if self.imagen_url:
            try:
                from urllib.request import Request, urlopen
                from urllib.error import URLError, HTTPError
                req = Request(self.imagen_url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
                resp = urlopen(req, timeout=5)
                ctype = resp.headers.get_content_type() if hasattr(resp.headers, 'get_content_type') else resp.headers.get('Content-Type', '')
                if not (ctype and ctype.startswith('image')):
                    raise ValidationError('La URL no apunta a un recurso de imagen.')
            except (HTTPError, URLError, ValueError):
                raise ValidationError('No se pudo acceder a la URL de la imagen.')
            except Exception:
                raise ValidationError('No se pudo validar la URL de la imagen.')



