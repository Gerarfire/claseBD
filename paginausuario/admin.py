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
    list_display = ('cargodesempenado', 'nombrempresa', 'fechainiciogestion', 'fechafingestion', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechainiciogestion', 'fechafingestion')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('cargodesempenado', 'nombrempresa', 'descripcionfunciones')
    ordering = ('-fechainiciogestion',)
    actions = ['activar_items', 'desactivar_items']

    def activar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=True)
        self.message_user(request, f"{queryset.count()} items activados.")
    activar_items.short_description = "Activar items seleccionados"

    def desactivar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=False)
        self.message_user(request, f"{queryset.count()} items desactivados.")
    desactivar_items.short_description = "Desactivar items seleccionados"

@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('tiporeconocimiento', 'descripcionreconocimiento', 'entidadpatrocinadora', 'fechareconocimiento', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'tiporeconocimiento', 'fechareconocimiento')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('tiporeconocimiento', 'descripcionreconocimiento', 'entidadpatrocinadora')
    ordering = ('-fechareconocimiento',)
    actions = ['activar_items', 'desactivar_items']

    def activar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=True)
        self.message_user(request, f"{queryset.count()} items activados.")
    activar_items.short_description = "Activar items seleccionados"

    def desactivar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=False)
        self.message_user(request, f"{queryset.count()} items desactivados.")
    desactivar_items.short_description = "Desactivar items seleccionados"

@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    list_display = ('nombrecurso', 'entidadpatrocinadora', 'fechainicio', 'totalhoras', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'entidadpatrocinadora', 'fechainicio')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('nombrecurso', 'entidadpatrocinadora', 'descripcioncurso')
    ordering = ('-fechainicio',)
    actions = ['activar_items', 'desactivar_items']

    def activar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=True)
        self.message_user(request, f"{queryset.count()} items activados.")
    activar_items.short_description = "Activar items seleccionados"

    def desactivar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=False)
        self.message_user(request, f"{queryset.count()} items desactivados.")
    desactivar_items.short_description = "Desactivar items seleccionados"

@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombrerecurso', 'clasificador', 'descripcion', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'clasificador')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('nombrerecurso', 'clasificador', 'descripcion')
    ordering = ('-nombrerecurso',)
    actions = ['activar_items', 'desactivar_items']

    def activar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=True)
        self.message_user(request, f"{queryset.count()} items activados.")
    activar_items.short_description = "Activar items seleccionados"

    def desactivar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=False)
        self.message_user(request, f"{queryset.count()} items desactivados.")
    desactivar_items.short_description = "Desactivar items seleccionados"

@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'fechaproducto', 'descripcion', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'fechaproducto')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('nombreproducto', 'descripcion')
    ordering = ('-fechaproducto',)
    actions = ['activar_items', 'desactivar_items']

    def activar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=True)
        self.message_user(request, f"{queryset.count()} items activados.")
    activar_items.short_description = "Activar items seleccionados"

    def desactivar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=False)
        self.message_user(request, f"{queryset.count()} items desactivados.")
    desactivar_items.short_description = "Desactivar items seleccionados"
