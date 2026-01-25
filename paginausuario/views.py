from django.shortcuts import render
from django.http import HttpResponse
from .models import DatosPersonales, ExperienciaLaboral, Reconocimiento, CursoRealizado, ProductoAcademico, ProductoLaboral, VentaGarage
from django.contrib.auth.models import User
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from io import BytesIO

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

def experiencias(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    experiencias = ExperienciaLaboral.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    context = {'perfil': perfil, 'experiencias': experiencias}
    return render(request, 'paginausuario/experiencias.html', context)

def reconocimientos(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    reconocimientos = Reconocimiento.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    context = {'perfil': perfil, 'reconocimientos': reconocimientos}
    return render(request, 'paginausuario/reconocimientos.html', context)

def cursos(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    cursos = CursoRealizado.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    context = {'perfil': perfil, 'cursos': cursos}
    return render(request, 'paginausuario/cursos.html', context)

def productos_academicos(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    productos_academicos = ProductoAcademico.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    context = {'perfil': perfil, 'productos_academicos': productos_academicos}
    return render(request, 'paginausuario/productos_academicos.html', context)

def productos_laborales(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    productos_laborales = ProductoLaboral.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    context = {'perfil': perfil, 'productos_laborales': productos_laborales}
    return render(request, 'paginausuario/productos_laborales.html', context)

def ventas_garage(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    ventas_garage = VentaGarage.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    context = {'perfil': perfil, 'ventas_garage': ventas_garage}
    return render(request, 'paginausuario/ventas_garage.html', context)

def experiencias_pdf(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    experiencias = ExperienciaLaboral.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=20)
    story.append(Paragraph(f"Experiencias Laborales - {perfil.nombres} {perfil.apellidos}", title_style))
    story.append(Spacer(1, 12))

    if experiencias:
        for exp in experiencias:
            story.append(Paragraph(f"<b>{exp.cargodesempenado}</b> en {exp.nombrempresa}", styles['Normal']))
            story.append(Paragraph(f"Lugar: {exp.lugarempresa}", styles['Normal']))
            story.append(Paragraph(f"Fecha Inicio: {exp.fechainiciogestion} - Fecha Fin: {exp.fechafingestion or 'Actualidad'}", styles['Normal']))
            story.append(Paragraph(f"Funciones: {exp.descripcionfunciones}", styles['Normal']))
            story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="experiencias_laborales.pdf"'
    return response

def reconocimientos_pdf(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    reconocimientos = Reconocimiento.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=20)
    story.append(Paragraph(f"Reconocimientos - {perfil.nombres} {perfil.apellidos}", title_style))
    story.append(Spacer(1, 12))

    if reconocimientos:
        for rec in reconocimientos:
            story.append(Paragraph(f"<b>{rec.tiporeconocimiento}</b>", styles['Normal']))
            story.append(Paragraph(f"Fecha: {rec.fechareconocimiento}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {rec.descripcionreconocimiento}", styles['Normal']))
            story.append(Paragraph(f"Entidad: {rec.entidadpatrocinadora}", styles['Normal']))
            story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reconocimientos.pdf"'
    return response

def cursos_pdf(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    cursos = CursoRealizado.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=20)
    story.append(Paragraph(f"Cursos Realizados - {perfil.nombres} {perfil.apellidos}", title_style))
    story.append(Spacer(1, 12))

    if cursos:
        for curso in cursos:
            story.append(Paragraph(f"<b>{curso.nombrecurso}</b>", styles['Normal']))
            story.append(Paragraph(f"Fecha Inicio: {curso.fechainicio} - Fecha Fin: {curso.fechafin or 'En curso'}", styles['Normal']))
            story.append(Paragraph(f"Horas: {curso.totalhoras}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {curso.descripcioncurso}", styles['Normal']))
            story.append(Paragraph(f"Entidad: {curso.entidadpatrocinadora}", styles['Normal']))
            story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cursos_realizados.pdf"'
    return response

def productos_academicos_pdf(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    productos_academicos = ProductoAcademico.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=20)
    story.append(Paragraph(f"Productos Académicos - {perfil.nombres} {perfil.apellidos}", title_style))
    story.append(Spacer(1, 12))

    if productos_academicos:
        for prod in productos_academicos:
            story.append(Paragraph(f"<b>{prod.nombrerecurso}</b>", styles['Normal']))
            story.append(Paragraph(f"Clasificador: {prod.clasificador}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {prod.descripcion}", styles['Normal']))
            story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="productos_academicos.pdf"'
    return response

def productos_laborales_pdf(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    productos_laborales = ProductoLaboral.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=20)
    story.append(Paragraph(f"Productos Laborales - {perfil.nombres} {perfil.apellidos}", title_style))
    story.append(Spacer(1, 12))

    if productos_laborales:
        for prod in productos_laborales:
            story.append(Paragraph(f"<b>{prod.nombreproducto}</b>", styles['Normal']))
            story.append(Paragraph(f"Fecha: {prod.fechaproducto}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {prod.descripcion}", styles['Normal']))
            story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="productos_laborales.pdf"'
    return response

def ventas_garage_pdf(request):
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")
    ventas_garage = VentaGarage.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=20)
    story.append(Paragraph(f"Ventas Garage - {perfil.nombres} {perfil.apellidos}", title_style))
    story.append(Spacer(1, 12))

    if ventas_garage:
        for venta in ventas_garage:
            story.append(Paragraph(f"<b>{venta.nombreproducto}</b>", styles['Normal']))
            story.append(Paragraph(f"Estado: {venta.estadoproducto}", styles['Normal']))
            story.append(Paragraph(f"Valor: ${venta.valordelbien}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {venta.descripcion}", styles['Normal']))
            story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ventas_garage.pdf"'
    return response

def hoja_vida_pdf(request):
    # Obtener el perfil activo
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    if not perfil:
        return HttpResponse("No hay perfil activo configurado.")

    experiencias = ExperienciaLaboral.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    reconocimientos = Reconocimiento.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    cursos = CursoRealizado.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    productos_academicos = ProductoAcademico.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)
    productos_laborales = ProductoLaboral.objects.filter(idperfilconqueestaactivo=perfil, activarparaqueseveaenfront=True)

    # Crear PDF con ReportLab
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Título
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, spaceAfter=20)
    story.append(Paragraph(f"Hoja de Vida - {perfil.nombres} {perfil.apellidos}", title_style))
    story.append(Spacer(1, 12))

    # Descripción
    story.append(Paragraph(f"<b>Descripción del Perfil:</b> {perfil.descripcionperfil}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Experiencias
    if experiencias:
        story.append(Paragraph("<b>Experiencia Laboral</b>", styles['Heading2']))
        for exp in experiencias:
            story.append(Paragraph(f"<b>{exp.cargodesempenado}</b> en {exp.nombrempresa}", styles['Normal']))
            story.append(Paragraph(f"Lugar: {exp.lugarempresa}", styles['Normal']))
            story.append(Paragraph(f"Fecha Inicio: {exp.fechainiciogestion} - Fecha Fin: {exp.fechafingestion or 'Actualidad'}", styles['Normal']))
            story.append(Paragraph(f"Funciones: {exp.descripcionfunciones}", styles['Normal']))
            story.append(Spacer(1, 12))

    # Reconocimientos
    if reconocimientos:
        story.append(Paragraph("<b>Reconocimientos</b>", styles['Heading2']))
        for rec in reconocimientos:
            story.append(Paragraph(f"<b>{rec.tiporeconocimiento}</b>", styles['Normal']))
            story.append(Paragraph(f"Fecha: {rec.fechareconocimiento}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {rec.descripcionreconocimiento}", styles['Normal']))
            story.append(Paragraph(f"Entidad: {rec.entidadpatrocinadora}", styles['Normal']))
            story.append(Spacer(1, 12))

    # Cursos
    if cursos:
        story.append(Paragraph("<b>Cursos Realizados</b>", styles['Heading2']))
        for curso in cursos:
            story.append(Paragraph(f"<b>{curso.nombrecurso}</b>", styles['Normal']))
            story.append(Paragraph(f"Fecha Inicio: {curso.fechainicio} - Fecha Fin: {curso.fechafin or 'En curso'}", styles['Normal']))
            story.append(Paragraph(f"Horas: {curso.totalhoras}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {curso.descripcioncurso}", styles['Normal']))
            story.append(Paragraph(f"Entidad: {curso.entidadpatrocinadora}", styles['Normal']))
            story.append(Spacer(1, 12))

    # Productos Académicos
    if productos_academicos:
        story.append(Paragraph("<b>Productos Académicos</b>", styles['Heading2']))
        for prod in productos_academicos:
            story.append(Paragraph(f"<b>{prod.nombrerecurso}</b>", styles['Normal']))
            story.append(Paragraph(f"Clasificador: {prod.clasificador}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {prod.descripcion}", styles['Normal']))
            story.append(Spacer(1, 12))

    # Productos Laborales
    if productos_laborales:
        story.append(Paragraph("<b>Productos Laborales</b>", styles['Heading2']))
        for prod in productos_laborales:
            story.append(Paragraph(f"<b>{prod.nombreproducto}</b>", styles['Normal']))
            story.append(Paragraph(f"Fecha: {prod.fechaproducto}", styles['Normal']))
            story.append(Paragraph(f"Descripción: {prod.descripcion}", styles['Normal']))
            story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)

    # Devolver como respuesta
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hoja_de_vida.pdf"'
    return response

def create_superuser(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("Superusuario 'admin' creado con contraseña 'admin123'. Ahora elimina esta URL.")
    else:
        return HttpResponse("El superusuario ya existe.")
