from django.shortcuts import render
from django.http import HttpResponse
from .models import DatosPersonales, ExperienciaLaboral, Reconocimiento, CursoRealizado, ProductoAcademico, ProductoLaboral
from django.contrib.auth.models import User

def pagina_bienvenida(request):
    return HttpResponse("<h1>HOJA DE VIDA</h1><a href='/hoja_vida/'>Ver Hoja de Vida</a>")

def hoja_vida(request):
    # Obtener el perfil activo (asumiendo perfilactivo=1)
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")

    # Obtener datos relacionados
    experiencias = ExperienciaLaboral.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    reconocimientos = Reconocimiento.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    cursos = CursoRealizado.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    productos_academicos = ProductoAcademico.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    productos_laborales = ProductoLaboral.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)

    context = {
        'perfil': perfil,
        'experiencias': experiencias,
        'reconocimientos': reconocimientos,
        'cursos': cursos,
        'productos_academicos': productos_academicos,
        'productos_laborales': productos_laborales,
    }
    return render(request, 'paginausuario/hoja_vida.html', context)

def create_superuser(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("Superusuario 'admin' creado con contraseña 'admin123'. Ahora elimina esta URL.")
    else:
        return HttpResponse("El superusuario ya existe.")
