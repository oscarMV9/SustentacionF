from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Produccion

def GeneratePDF(modelAdmin, request, queryset):
    # Crea la respuesta HTTP con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Produccion.pdf"'

    c = canvas.Canvas(response, pagesize=letter)

    # Comienza a dibujar el texto
    textObject = c.beginText(40, 750)  # Ubicación inicial del texto
    textObject.setFont("Helvetica-Bold", 12)

    # Título del reporte
    textObject.textLine("Reporte de Produccion")
    textObject.textLine("="*50)
    textObject.setFont("Helvetica", 12)

    # Datos de Producción
    for produccion in queryset:  # Aquí pasamos el queryset, que es el filtro de la vista admin
        textObject.setFont("Helvetica-Bold", 12)
        textObject.textLine(f"ID Producción: {produccion.idProduccion}")
        textObject.setFont("Helvetica", 12)
        textObject.textLine(f"Nombre Producto: {produccion.nombreProducto}")
        textObject.textLine(f"Descripción: {produccion.descripcion}")
        textObject.textLine(f"Proveedor: {produccion.nombreProveedor}")
        textObject.textLine(f"Cantidad: {produccion.cantidad}")
        textObject.textLine(f"Materiales: {produccion.materiales}")
        textObject.textLine(f"Costo Producción: {produccion.costoProduccion}")
        textObject.textLine(f"Fecha Finalización: {produccion.fecha_finalizacion}")
        textObject.textLine("="*50)



    c.drawText(textObject)
    c.showPage()  # Nueva página (si es necesario)
    c.save()

    return response

GeneratePDF.short_description = "Generar reporte PDF de Producción"


class ProduccionResource(resources.ModelResource):
    class Meta:
        model = Produccion
        fields = ('idProduccion', 'nombreProducto', 'descripcion', 'nombreProveedor', 'cantidad', 'materiales', 'costoProduccion', 'fecha_finalizacion')  # Campos para exportar/importar
        export_order = ('idProduccion', 'nombreProducto', 'descripcion', 'nombreProveedor', 'cantidad', 'materiales', 'costoProduccion', 'fecha_finalizacion')  # Orden de columnas

@admin.register(Produccion)
class ProduccionAdmin(ImportExportModelAdmin):
    resource_class = ProduccionResource
    list_display = ('idProduccion', 'nombreProducto', 'nombreProveedor', 'cantidad', 'costoProduccion', 'fecha_finalizacion')  # Campos visibles en el admin
    search_fields = ('nombreProducto', 'nombreProveedor') 
    list_filter = ('fecha_finalizacion', 'nombreProveedor')
    actions = [GeneratePDF]