"""
Formularios para la aplicación paginausuario
"""
from django import forms
from .models import DatosPersonales, ExperienciaLaboral, CursoRealizado, Reconocimiento, ProductoAcademico, ProductoLaboral


class DatosPersonalesForm(forms.ModelForm):
    """Formulario para datos personales"""
    class Meta:
        model = DatosPersonales
        fields = ['nombres', 'apellidos', 'descripcionperfil', 'foto_perfil', 'foto_perfil_url', 'telefonoconvencional', 'telefonofijo', 'direcciondomiciliaria', 'sitioweb']


class ExperienciaLaboralForm(forms.ModelForm):
    """Formulario para experiencia laboral"""
    class Meta:
        model = ExperienciaLaboral
        fields = ['cargodesempenado', 'nombrempresa', 'lugarempresa', 'emailempresa', 'sitiowebempresa', 'fechainiciogestion', 'fechafingestion', 'descripcionfunciones', 'activarparaqueseveaenfront']


class CursoRealizadoForm(forms.ModelForm):
    """Formulario para cursos realizados"""
    class Meta:
        model = CursoRealizado
        fields = ['nombrecurso', 'fechainicio', 'fechafin', 'totalhoras', 'descripcioncurso', 'entidadpatrocinadora', 'activarparaqueseveaenfront']


class ReconocimientoForm(forms.ModelForm):
    """Formulario para reconocimientos"""
    class Meta:
        model = Reconocimiento
        fields = ['tiporeconocimiento', 'fechareconocimiento', 'descripcionreconocimiento', 'entidadpatrocinadora', 'activarparaqueseveaenfront']


class ProductoAcademicoForm(forms.ModelForm):
    """Formulario para productos académicos"""
    class Meta:
        model = ProductoAcademico
        fields = ['nombrerecurso', 'clasificador', 'descripcion', 'activarparaqueseveaenfront']


class ProductoLaboralForm(forms.ModelForm):
    """Formulario para productos laborales"""
    class Meta:
        model = ProductoLaboral
        fields = ['nombreproducto', 'fechaproducto', 'descripcion', 'activarparaqueseveaenfront']


class VentaGarageForm(forms.ModelForm):
    """Formulario para ventas garage con soporte de imagen y validación"""
    class Meta:
        model = __import__('paginausuario.models', fromlist=['VentaGarage']).VentaGarage
        fields = ['nombreproducto', 'estadoproducto', 'descripcion', 'imagen', 'imagen_url', 'valordelbien', 'activarparaqueseveaenfront']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows':2}),
        }

    def clean_imagen(self):
        img = self.cleaned_data.get('imagen')
        if not img:
            return img
        # Size limit: 5 MB
        max_size = 5 * 1024 * 1024
        if hasattr(img, 'size') and img.size > max_size:
            raise forms.ValidationError('El archivo es demasiado grande (máx 5 MB).')
        # Validate format and dimensions
        try:
            from PIL import Image
            img.seek(0)
            image = Image.open(img)
            fmt = (image.format or '').upper()
            if fmt not in ('JPEG', 'PNG'):
                raise forms.ValidationError('Formato no soportado. Use JPEG o PNG.')
            max_dim = 4000
            if image.width > max_dim or image.height > max_dim:
                raise forms.ValidationError('Dimensiones demasiado grandes (máx 4000x4000).')
        except forms.ValidationError:
            raise
        except Exception:
            raise forms.ValidationError('No se pudo procesar la imagen.')
        finally:
            try:
                img.seek(0)
            except Exception:
                pass
        return img

    def clean_imagen_url(self):
        url = self.cleaned_data.get('imagen_url')
        if not url:
            return url
        try:
            from urllib.request import Request, urlopen
            from urllib.error import URLError, HTTPError
            req = Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
            resp = urlopen(req, timeout=5)
            ctype = resp.headers.get_content_type() if hasattr(resp.headers, 'get_content_type') else resp.headers.get('Content-Type', '')
            if not (ctype and ctype.startswith('image')):
                raise forms.ValidationError('La URL no apunta a un recurso de imagen.')
        except (HTTPError, URLError, ValueError):
            raise forms.ValidationError('No se pudo acceder a la URL proporcionada.')
        except Exception:
            raise forms.ValidationError('No se pudo validar la URL de la imagen.')
        return url