from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Productos, Inventario

class ProductosResource(resources.ModelResource):
    class Meta:
        model = Productos

class InventarioResource(resources.ModelResource):
    class Meta:
        model = Inventario

@admin.register(Productos)
class ProductosAdmin(ImportExportModelAdmin):
    resource_class = ProductosResource
    list_display = ('id', 'idProducto','imagen', 'descripcion', 'precio')
    search_fields = ('descripcion',)

@admin.register(Inventario)
class InventarioAdmin(ImportExportModelAdmin):
    resource_class = InventarioResource
    list_display = ('id', 'idProducto','descripcion')
    search_fields = ('descripcion',)