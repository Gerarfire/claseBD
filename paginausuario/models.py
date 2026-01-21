from django.db import models

#BD tabla datos_personales
class DatosPersonales(models.Model):
    idperfil = models.AutoField(primary_key=True)
    descripcionperfil = models.CharField(max_length=50)
    perfilactivo = models.IntegerField()
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)

    class Meta:
        db_table = 'datos_personales'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

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
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'experiencialaboral'

    def __str__(self):
        return f"{self.cargodesempenado} - {self.nombrempresa}"


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
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'reconocimientos'

    def __str__(self):
        return f"{self.tiporeconocimiento} - {self.entidadpatrocinadora}"

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
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'cursosrealizados'

    def __str__(self):
        return f"{self.nombrecurso} ({self.totalhoras} horas)"


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
    activarparaqueseveaenfront = models.BooleanField(default=True)

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
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = 'productoslaborales'

    def __str__(self):
        return self.nombreproducto


#BD tabla venta garage
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
    valordelbien = models.DecimalField(max_digits=5, decimal_places=2)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = 'ventagarage'

    def __str__(self):
        return self.nombreproducto
