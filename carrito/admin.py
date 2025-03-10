from django.contrib import admin
from .models import Orden, OrdenItem
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from produccion.models import Produccion
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from import_export import resources
from import_export.admin import ExportMixin
from io import BytesIO

def pdf_orden(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ordenes.pdf"'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']

    # Agregar un título
    elements.append(Paragraph("Reporte de Órdenes", styleH))

    for orden in queryset:
        # Agregar información de la orden
        elements.append(Paragraph(f"ID: {orden.id}", styleN))
        elements.append(Paragraph(f"Nombre del cliente: {orden.nombre_cliente}", styleN))
        elements.append(Paragraph(f"Número de documento: {orden.N_documento}", styleN))
        elements.append(Paragraph(f"Teléfono: {orden.telefono}", styleN))
        elements.append(Paragraph(f"Dirección de envío: {orden.direccion}", styleN))
        elements.append(Paragraph(f"Fecha de pedido: {orden.fecha}", styleN))
        elements.append(Paragraph(f"Correo Email: {orden.email}", styleN))
        elements.append(Paragraph(f"Total de la compra: {orden.total}", styleN))
        elements.append(Paragraph(f"Estado de la compra: {orden.status}", styleN))

        data = [["Producto", "Cantidad", "Precio Unitario", "Total"]]
        for item in orden.items.all():
            try:
                producto_nombre = item.producto.idProducto.get_nombre_producto()
            except Produccion.DoesNotExist:
                producto_nombre = "Producto no disponible"
            data.append([producto_nombre, item.cantidad, item.precio_unitario, item.cantidad * item.precio_unitario])

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        elements.append(Paragraph("<br/><br/>", styleN))  

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

pdf_orden.short_description = "Exportar a PDF"

class OrdenResource(resources.ModelResource):
    class Meta:
        model = Orden

@admin.register(Orden)
class OrdenAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = OrdenResource
    list_display = ('id', 'nombre_cliente', 'N_documento', 'telefono', 'direccion', 'fecha', 'email', 'status', 'total')
    search_fields = ('nombre_cliente', 'N_documento', 'telefono', 'email')
    list_filter = ('status', 'fecha')
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
    actions = [pdf_orden]

@admin.register(OrdenItem)
class OrdenItemAdmin(admin.ModelAdmin):
    list_display = ('orden', 'producto', 'cantidad', 'precio_unitario')
    search_fields = ('orden__nombre_cliente', 'producto__nombre')
    list_filter = ('orden__fecha',)
    ordering = ('-orden__fecha',)