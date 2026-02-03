from django.contrib import admin
from .models import DatosPersonales, ExperienciaLaboral, Reconocimiento, CursoRealizado, ProductoAcademico, ProductoLaboral, VentaGarage
from .forms import VentaGarageForm

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
    actions = ['set_active_profile']

    def set_active_profile(self, request, queryset):
        # Set the first selected profile as active and deactivate all others
        if not queryset.exists():
            self.message_user(request, 'No profiles selected.')
            return
        profile = queryset.first()
        # deactivate all
        DatosPersonales.objects.update(perfilactivo=0)
        profile.perfilactivo = 1
        profile.save()
        self.message_user(request, f'Perfil "{profile}" marcado como activo.')
    set_active_profile.short_description = 'Marcar el perfil seleccionado como activo'

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

@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    form = VentaGarageForm
    list_display = ('nombreproducto', 'estadoproducto', 'imagen_preview', 'descripcion', 'valordelbien', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'estadoproducto')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('nombreproducto', 'descripcion')
    ordering = ('-nombreproducto',)
    readonly_fields = ('imagen_preview',)
    fields = ('idperfilconqueestaactivo', 'nombreproducto', 'estadoproducto', 'descripcion', 'imagen', 'valordelbien', 'activarparaqueseveaenfront')
    actions = ['activar_items', 'desactivar_items']

    from django.utils.html import format_html

    def imagen_preview(self, obj):
        try:
            if obj.imagen and getattr(obj.imagen, 'url', None):
                return format_html("<img src='{}' width='80' style='object-fit:cover;border-radius:6px;'/>", obj.imagen.url)
        except Exception:
            # Evitar que errores del backend de storage rompan el admin
            return '(error al mostrar imagen)'
        return '(sin imagen)'
    imagen_preview.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        from django.contrib import messages
        import logging
        from django.core.exceptions import ValidationError
        logger = logging.getLogger(__name__)
        try:
            # Ejecutar validación del modelo antes de guardar para capturar problemas de imagen
            obj.full_clean()
            super().save_model(request, obj, form, change)
        except ValidationError as e:
            logger.exception('Validation error saving VentaGarage')
            self.message_user(request, '; '.join(e.messages), level=messages.ERROR)
        except Exception as e:
            logger.exception('Error guardando VentaGarage')
            # Mostrar mensaje amable en admin en vez de 500
            self.message_user(request, f"Error al guardar la venta: {e}", level=messages.ERROR)

    def activar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=True)
        self.message_user(request, f"{queryset.count()} items activados.")
    activar_items.short_description = "Activar items seleccionados"

    def desactivar_items(self, request, queryset):
        queryset.update(activarparaqueseveaenfront=False)
        self.message_user(request, f"{queryset.count()} items desactivados.")
    desactivar_items.short_description = "Desactivar items seleccionados"
