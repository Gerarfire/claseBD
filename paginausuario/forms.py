"""
Formularios para la aplicación paginausuario
"""
from django import forms
from .models import DatosPersonales, ExperienciaLaboral, CursoRealizado, Reconocimiento, ProductoAcademico, ProductoLaboral


class DatosPersonalesForm(forms.ModelForm):
    """Formulario para datos personales"""
    class Meta:
        model = DatosPersonales
        fields = ['nombre', 'apellido', 'email', 'telefono', 'foto_perfil', 'direcciondomiciliaria', 'ciudad', 'pais']


class ExperienciaLaboralForm(forms.ModelForm):
    """Formulario para experiencia laboral"""
    class Meta:
        model = ExperienciaLaboral
        fields = ['empresa', 'puesto', 'descripcion', 'fecha_inicio', 'fecha_fin']


class CursoRealizadoForm(forms.ModelForm):
    """Formulario para cursos realizados"""
    class Meta:
        model = CursoRealizado
        fields = ['titulo', 'institucion', 'fecha_finalizacion', 'certificado']


class ReconocimientoForm(forms.ModelForm):
    """Formulario para reconocimientos"""
    class Meta:
        model = Reconocimiento
        fields = ['titulo', 'descripcion', 'fecha_otorgamiento']


class ProductoAcademicoForm(forms.ModelForm):
    """Formulario para productos académicos"""
    class Meta:
        model = ProductoAcademico
        fields = ['titulo', 'descripcion', 'enlace', 'fecha_publicacion']


class ProductoLaboralForm(forms.ModelForm):
    """Formulario para productos laborales"""
    class Meta:
        model = ProductoLaboral
        fields = ['titulo', 'descripcion', 'enlace', 'fecha_publicacion']