from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Venta, VentaItem

def GeneratePDFVentas(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Ventas.pdf"'
    
    c = canvas.Canvas(response, pagesize=letter)
    
    text_object = c.beginText(40, 750)  
    text_object.setFont("Helvetica-Bold", 12)

    text_object.textLine("Reporte de Ventas")
    text_object.textLine("="*50)

    for venta in queryset:
        text_object.setFont("Helvetica-Bold", 12)
        text_object.textLine(f"ID Venta: {venta.idVenta}")
        text_object.setFont("Helvetica", 12)
        text_object.textLine(f"Cliente: {venta.nombre_cliente} {venta.apellido_cliente}")
        text_object.textLine(f"Fecha: {venta.fecha}")
        text_object.textLine(f"Total: ${venta.total:.2f}")
        text_object.textLine("="*50)
        
        text_object.setFont("Helvetica-Bold", 12)
        text_object.textLine(f"Detalles de los Productos:")
        text_object.setFont("Helvetica", 12)

        for item in venta.items.all():
            text_object.textLine(f"  Producto: {item.producto.idProducto.get_nombre_producto()}")
            text_object.textLine(f"  Cantidad: {item.cantidad}")
            text_object.textLine(f"  Precio Unitario: ${item.precio_unitario:.2f}")
            text_object.textLine(f"  Subtotal: ${item.subtotal:.2f}")
            text_object.textLine("-" * 50)

    c.drawText(text_object)
    c.showPage()
    c.save()
    
    return response

GeneratePDFVentas.short_description = "Generar reporte PDF de Ventas"

# Recurso para exportar datos de ventas
class VentaResource(resources.ModelResource):
    class Meta:
        model = Venta
        fields = ('idVenta', 'nombre_cliente', 'apellido_cliente', 'fecha', 'total') 
        export_order = ('idVenta', 'nombre_cliente', 'apellido_cliente', 'fecha', 'total')

# Inline para mostrar los productos (VentaItem) dentro de la venta
class VentaItemInline(admin.TabularInline):
    model = VentaItem
    extra = 1  # Muestra un formulario extra para agregar productos
    fields = ('producto', 'cantidad', 'precio_unitario')
    readonly_fields = ('subtotal',)  # Para que no sea editable el subtotal
    can_delete = True

    def subtotal(self, obj):
        return obj.subtotal
    subtotal.short_description = "Subtotal"

# Admin de la clase Venta
@admin.register(Venta)
class VentasAdmin(ImportExportModelAdmin):
    list_display = ('idVenta', 'get_cliente_nombre', 'fecha', 'total')  
    search_fields = ('nombre_cliente', 'idVenta', 'cedula')
    actions = [GeneratePDFVentas]
    inlines = [VentaItemInline]  # Agregamos el inline para los productos asociados a la venta

    def fecha(self, obj):
        return obj.fecha 
    fecha.admin_order_field = 'fecha'  

    def get_cliente_nombre(self, obj):
        return f"{obj.nombre_cliente} {obj.apellido_cliente}"
    get_cliente_nombre.short_description = 'Cliente'



