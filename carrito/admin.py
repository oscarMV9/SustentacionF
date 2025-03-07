from django.contrib import admin
from .models import Orden, OrdenItem
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from import_export import resources
from import_export.admin import ExportMixin
from io import BytesIO

def pdf_orden(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ordenes.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    y = height - 40
    for orden in queryset:
        p.drawString(30, y, f"Orden ID: {orden.id}")
        p.drawString(30, y - 20, f"Cliente: {orden.nombre_cliente}")
        p.drawString(30, y - 40, f"Documento: {orden.N_documento}")
        p.drawString(30, y - 60, f"Teléfono: {orden.telefono}")
        p.drawString(30, y - 80, f"Dirección: {orden.direccion}")
        p.drawString(30, y - 100, f"Fecha: {orden.fecha}")
        p.drawString(30, y - 120, f"Email: {orden.email}")
        p.drawString(30, y - 140, f"Status: {orden.status}")
        p.drawString(30, y - 160, f"Total: {orden.total}")
        y -= 200

        if y < 40:
            p.showPage()
            y = height - 40

    p.save()
    buffer.seek(0)
    response.write(buffer.read())
    buffer.close()
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