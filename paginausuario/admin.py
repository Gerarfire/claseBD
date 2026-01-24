from django.contrib import admin
from .models import DatosPersonales, ExperienciaLaboral, Reconocimiento, CursoRealizado, ProductoAcademico, ProductoLaboral

# Register your models here.

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'descripcionperfil', 'numerocedula', 'sexo', 'perfilactivo')
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombres', 'apellidos', 'descripcionperfil', 'foto_perfil', 'perfilactivo')
        }),
        ('Información Personal', {
            'fields': ('nacionalidad', 'lugarnacimiento', 'fechanacimiento', 'numerocedula', 'sexo', 'estadocivil', 'licenciaconducir')
        }),
        ('Contacto', {
            'fields': ('telefonoconvencional', 'telefonofijo', 'sitioweb')
        }),
        ('Direcciones', {
            'fields': ('direcciontrabajo', 'direcciondomiciliaria')
        }),
    )

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('cargodesempenado', 'nombrempresa', 'fechainiciogestion', 'fechafingestion')

@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('tiporeconocimiento', 'descripcionreconocimiento', 'entidadpatrocinadora', 'fechareconocimiento')

@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    list_display = ('nombrecurso', 'entidadpatrocinadora', 'fechainicio', 'totalhoras')

@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombrerecurso', 'clasificador', 'descripcion')

@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'fechaproducto', 'descripcion')
