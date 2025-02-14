from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Produccion 

class ProduccionResource(resources.ModelResource):
    class Meta:
        model = Produccion
        fields = ('idProduccion', 'nombreProducto', 'descripcion', 'nombreProveedor', 'cantidad', 'materiales', 'costoProduccion', 'fecha_finalizacion')  # Campos para exportar/importar
        export_order = ('idProduccion', 'nombreProducto', 'descripcion', 'nombreProveedor', 'cantidad', 'materiales', 'costoProduccion', 'fecha_finalizacion')  # Orden de columnas

# Configurar el admin con ImportExportModelAdmin
@admin.register(Produccion)
class ProduccionAdmin(ImportExportModelAdmin):
    resource_class = ProduccionResource
    list_display = ('idProduccion', 'nombreProducto', 'nombreProveedor', 'cantidad', 'costoProduccion', 'fecha_finalizacion')  # Campos visibles en el admin
    search_fields = ('nombreProducto', 'nombreProveedor') 
    list_filter = ('fecha_finalizacion', 'nombreProveedor')  

