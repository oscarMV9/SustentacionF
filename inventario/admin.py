from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Productos, Inventario
from django.contrib import messages

# Funcion para generar PDF para inventario
def GeneratePDFInventario(modelAdmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Inventario.pdf"'

    c = canvas.Canvas(response, pagesize=letter)

    textObject = c.beginText(40, 750)  
    textObject.setFont("Helvetica-Bold", 12)

    textObject.textLine("Reporte de Inventario")
    textObject.textLine("="*50)
    textObject.setFont("Helvetica", 12)

    for inventario in queryset:
        producto = inventario.idProducto 

        textObject.setFont("Helvetica-Bold", 12)
        textObject.textLine(f"ID Inventario: {inventario.id}")
        textObject.setFont("Helvetica", 12)
        textObject.textLine(f"ID Producto: {producto.id}")
        textObject.textLine(f"Descripción Producto: {producto.descripcion}")
        textObject.textLine(f"Precio Producto: {producto.precio}")

        textObject.textLine(f"Cantidad en Inventario: {inventario.cantidades}")
        textObject.textLine("="*50)

    c.drawText(textObject)
    c.showPage()
    c.save()

    return response

GeneratePDFInventario.short_description = "Generar reporte PDF de Inventario"

def GeneratePDFProductos(modelAdmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Productos.pdf"'

    c = canvas.Canvas(response, pagesize=letter)

    textObject = c.beginText(40, 750)  
    textObject.setFont("Helvetica-Bold", 12)

    textObject.textLine("Reporte de Productos")
    textObject.textLine("="*50)
    textObject.setFont("Helvetica", 12)

    for producto in queryset:
        textObject.setFont("Helvetica-Bold", 12)
        textObject.textLine(f"ID Producto: {producto.id}")
        textObject.setFont("Helvetica", 12)
        textObject.textLine(f"Descripción Producto: {producto.descripcion}")
        textObject.textLine(f"Precio Producto: {producto.precio}")
        textObject.textLine("="*50)

    c.drawText(textObject)
    c.showPage()
    c.save()

    return response

GeneratePDFProductos.short_description = "Generar reporte PDF de Productos"


class ProductosResource(resources.ModelResource):
    class Meta:
        model = Productos


class InventarioResource(resources.ModelResource):
    class Meta:
        model = Inventario


@admin.register(Productos)
class ProductosAdmin(ImportExportModelAdmin):
    resource_class = ProductosResource
    list_display = ('id', 'idProducto', 'imagen', 'descripcion', 'precio', 'precio_compra_unitario_de_fabrica')
    search_fields = ('descripcion',)
    actions = [GeneratePDFProductos] 
 

@admin.register(Inventario)
class InventarioAdmin(ImportExportModelAdmin):
    resource_class = InventarioResource
    list_display = ('id', 'idProducto', 'descripcion' ,'nombre_proveedor','stock_minimo', 'cantidades', 'stock_maximo','precio_de_fabrica','precio_de_venta','ganancias_totales','categoriaTalla', 'categoriaColor', 'categoriaPrenda', 'categoriaGenero', 'alerta_stock')
    search_fields = ('descripcion',)
    actions = [GeneratePDFInventario]

    def alerta_stock(self, obj):
        if obj.cantidades <= obj.stock_minimo + 5:
            return "⚠️ STOCK BAJO"
        return "✅ OK"
    alerta_stock.short_description = 'Alerta'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.cantidades <= obj.stock_minimo:
            messages.warning(
                request,
                f'ALERTA: Stock bajo para "{obj.idProducto}" - {obj.cantidades} unidades (Mínimo: {obj.stock_minimo})'
            )