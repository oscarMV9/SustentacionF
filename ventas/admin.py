from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Venta

def GeneratePDFVentas(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Logistica.pdf"'
    
    c = canvas.Canvas(response, pagesize=letter)
    
    text_object = c.beginText(40, 750)  
    text_object.setFont("Helvetica-Bold", 12)

    text_object.textLine("Reporte de Ventas")
    text_object.textLine("="*50)

    for venta in queryset:
        text_object.setFont("Helvetica-Bold", 12)
        text_object.textLine(f"ID Venta: {venta.idVenta}")
        text_object.setFont("Helvetica", 12)
        text_object.textLine(f"Cliente: {venta.cliente.nombre} {venta.cliente.apellido}")
        text_object.textLine(f"Fecha: {venta.fechaPedido}") 
        text_object.textLine("="*50)
        
        text_object.setFont("Helvetica-Bold", 12)
        text_object.textLine(f"Cliente Detalles:")
        text_object.setFont("Helvetica", 12)
        text_object.textLine(f"  Nombre: {venta.cliente.nombre} {venta.cliente.apellido}")
        text_object.textLine(f"  Email: {venta.cliente.email}")
        text_object.textLine(f"  Teléfono: {venta.cliente.telefono}")
        text_object.textLine(f"  Dirección: {venta.cliente.direccion if venta.cliente.direccion else 'N/A'}")
        text_object.textLine("="*50)
        
    c.drawText(text_object)
    c.showPage()
    c.save()
    
    return response

GeneratePDFVentas.short_description = "Generar reporte PDF de Ventas"

def GeneratePDFClientes(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Logistica.pdf"'

    
    c = canvas.Canvas(response, pagesize=letter)
    
    text_object = c.beginText(40, 750)  
    text_object.setFont("Helvetica-Bold", 12)

    text_object.textLine("Reporte de Clientes")
    text_object.textLine("="*50)
    
    for cliente in queryset:
        text_object.setFont("Helvetica-Bold", 12)
        text_object.textLine(f"ID Cliente: {cliente.idCliente}")
        text_object.setFont("Helvetica", 12)
        text_object.textLine(f"Nombre: {cliente.nombre} {cliente.apellido}")
        text_object.textLine(f"Email: {cliente.email}")
        text_object.textLine(f"Teléfono: {cliente.telefono}")
        text_object.textLine(f"Dirección: {cliente.direccion if cliente.direccion else 'N/A'}")
        text_object.textLine("="*50)
        
    c.drawText(text_object)
    c.showPage()
    c.save()
    
    return response

GeneratePDFClientes.short_description = "Generar reporte PDF de Clientes"

class VentaResource(resources.ModelResource):
    class Meta:
        model = Venta
        fields = ('idVenta', 'cliente', 'fechaPedido', 'total') 
        export_order = ('idVenta', 'cliente', 'fechaPedido', 'total')

@admin.register(Venta)
class VentasAdmin(ImportExportModelAdmin):
    list_display = ('idVenta', 'get_cliente_nombre', 'fechaPedido', 'total')  
    search_fields = ('cliente__nombre', 'idVenta')
    actions = [GeneratePDFVentas]  

    def fechaPedido(self, obj):
        return obj.fechaPedido 
    fechaPedido.admin_order_field = 'fechaPedido'  

    def get_cliente_nombre(self, obj):
        return f"{obj.cliente.nombre} {obj.cliente.apellido}"
    get_cliente_nombre.short_description = 'Cliente'
