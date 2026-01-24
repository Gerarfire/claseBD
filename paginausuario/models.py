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
    descripcionperfil = models.CharField(max_length=50)
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

    class Meta:
        db_table = 'datospersonales'

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



