from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Transportista, Logistica
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe

# Función para generar el reporte PDF de Logística
def GeneratePDFLogistica(modelAdmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Logistica.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
    textObject = c.beginText(40, 750)
    textObject.setFont("Helvetica-Bold", 12)

    textObject.textLine("Reporte de Logística")
    textObject.textLine("="*50)
    textObject.setFont("Helvetica", 12)

    for logistica in queryset:
        # Información de la logística
        textObject.setFont("Helvetica-Bold", 12)
        textObject.textLine(f"ID Logística: {logistica.idLogistica}")
        textObject.setFont("Helvetica", 12)
        textObject.textLine(f"Transportista: {logistica.transportista.nombres} {logistica.transportista.apellidos}")
        textObject.textLine(f"Costo Envío: {logistica.costoEnvio}")
        textObject.textLine(f"Dirección: {logistica.direccion}")
        
        # Agregar los productos dentro de la misma función para personalizarlos
        productos = logistica.get_productos()  # Obtener productos de la orden asociada
        textObject.setFont("Helvetica-Bold", 10)
        textObject.textLine("Productos:")

        # Aquí es donde puedes aplicar diseño personalizado a los productos
        for producto in productos:
            textObject.setFont("Helvetica-Bold", 12)
            textObject.textLine(f"- {producto['producto']}")
            textObject.setFont("Helvetica", 10)
            textObject.textLine(f"  Cantidad: {producto['cantidad']}, Precio Unitario: {producto['precio_unitario']}, Total: {producto['total']}")
        
        textObject.textLine("="*50)

    c.drawText(textObject)
    c.showPage()
    c.save()
    return response

GeneratePDFLogistica.short_description = "Generar reporte PDF de Logistica"

# Función para generar el reporte PDF de Transportista
def GeneratePDFTransportista(modelAdmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Transportista.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
    textObject = c.beginText(40, 750)
    textObject.setFont("Helvetica-Bold", 12)

    textObject.textLine("Reporte de Transportistas")
    textObject.textLine("="*50)
    textObject.setFont("Helvetica", 12)

    for transportista in queryset:
        textObject.setFont("Helvetica-Bold", 12)
        textObject.textLine(f"ID Transportista: {transportista.idTransportista}")
        textObject.setFont("Helvetica", 12)
        textObject.textLine(f"Nombre: {transportista.nombres} {transportista.apellidos}")
        textObject.textLine(f"Teléfono: {transportista.telefono}")
        textObject.textLine(f"Estado: {transportista.estado}")
        textObject.textLine("="*50)

    c.drawText(textObject)
    c.showPage()
    c.save()
    return response

GeneratePDFTransportista.short_description = "Generar reporte PDF de Transportistas"


# Resource de Logística para Import-Export
class LogisticaResource(resources.ModelResource):
    class Meta:
        model = Logistica
        fields = ('idLogistica', 'costoEnvio', 'transportista', 'direccion')


# Registro de la clase TransportistaAdmin
@admin.register(Transportista)
class TransportistaAdmin(admin.ModelAdmin):
    list_display = ('idTransportista', 'nombres', 'apellidos', 'telefono', 'estado')
    search_fields = ('nombres', 'apellidos', 'telefono')
    list_filter = ('estado',)
    actions = [GeneratePDFTransportista]


# Registro de la clase LogisticaAdmin
class LogisticaAdmin(admin.ModelAdmin):
    list_display = ('idLogistica', 'transportista', 'costoEnvio', 'direccion')
    search_fields = ('transportista__nombres', 'direccion')
    list_filter = ('transportista__estado',)

    # Para solo lectura del campo 'productos' en el admin
    readonly_fields = ('productos',)

    # Mostrar los productos en la vista de la administración de Logística
    def productos(self, obj):
        productos = obj.get_productos()
        productos_text = ""
        for producto in productos:
            productos_text += f"{producto['producto']} (Cantidad: {producto['cantidad']}, Precio: {producto['precio_unitario']}, Total: {producto['total']})<br>"
        return mark_safe(productos_text)

    productos.short_description = 'Productos de la Orden'

    # Acción para generar el PDF
    actions = [GeneratePDFLogistica]


# Registrar el modelo Logistica en el admin
admin.site.register(Logistica, LogisticaAdmin)
