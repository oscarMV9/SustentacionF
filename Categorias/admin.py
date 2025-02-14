from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from import_export.admin import ImportExportModelAdmin
from .models import CategoriaColor, CategoriaGenero, CategoriaPrenda, CategoriaTalla

def GeneratePDF(modelAdmin, request,queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-disposition'] = 'attachment; filename="reporte_categorias.pdf"'

    p = canvas.Canvas(response,pagesize=letter)
    textObject = p.beginText(40,750)
    textObject.setFont("Helvetica",12)

    textObject.textLine("reporte de categorias")
    textObject.textLine("="*50)

    textObject.textLine("\nCategorias de prendas: ")
    for categoria in CategoriaPrenda.objects.all():
        textObject.textLine(f" - {categoria.nombreCategoria}")

    textObject.textLine("="*50)

    textObject.textLine("\nCategorias generos: ")
    for categoria in CategoriaGenero.objects.all():
        textObject.textLine(f" - tipo: {categoria.genero}")

    textObject.textLine("="*50)

    textObject.textLine("\nCategorias de Tallas:")
    for categoria in CategoriaTalla.objects.all():
        textObject.textLine(f"- Tipo: {categoria.tipoTalla}, Talla: {categoria.talla}")

    textObject.textLine("="*50)

    textObject.textLine("\nCategorias colores: ")
    for categoria in CategoriaColor.objects.all():
        textObject.textLine(f"- {categoria.color}")

    p.drawText(textObject)
    p.showPage()
    p.save()

    return response

GeneratePDF.short_description = "generar reporte PDF de categorias"

@admin.register(CategoriaPrenda)
class CategoriaPrendaAdmin(ImportExportModelAdmin):
    list_display = ('nombreCategoria',)
    search_fields = ('nombreCategoria',)
    actions = [GeneratePDF]

@admin.register(CategoriaColor)
class CategoriaColorAdmin(ImportExportModelAdmin):
    list_display = ('color',)
    search_fields = ('color',)
    actions = [GeneratePDF]

@admin.register(CategoriaGenero)
class CategoriaGeneroAdmin(ImportExportModelAdmin):
    list_display = ('genero',)
    search_fields = ('genero',)
    actions = [GeneratePDF]

@admin.register(CategoriaTalla)
class CategoriaTallaAdmin(ImportExportModelAdmin):
    list_display = ('tipoTalla', 'talla',)
    search_fields = ('talla',)
    actions = [GeneratePDF]