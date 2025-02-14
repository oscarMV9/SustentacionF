from django.contrib import admin
from .models import transportistas, VentaPedido, logistica
from import_export import resources
from import_export.admin import ExportMixin

class LogisticaResource(resources.ModelResource):
    class Meta:
        model = logistica
        fields = ('idLogistica', 'ventapedidoId', 'costoEnvio', 'transportista', 'direccion')  # Campos exportables
        export_order = ('idLogistica', 'ventapedidoId', 'transportista', 'costoEnvio', 'direccion')


class TransportistaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'telefono', 'estado')
    search_fields = ('nombres', 'apellidos', 'estado')
    list_filter = ('estado',)

class VentaPedidoAdmin(admin.ModelAdmin):
    list_display = ('idVentaPedido', 'nombresCliente', 'apellidosCliente', 'cantidad', 'total', 'fechaPedido', 'direccion')
    search_fields = ('nombresCliente', 'apellidosCliente', 'direccion')
    list_filter = ('fechaPedido',)

class LogisticaAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = LogisticaResource
    list_display = ('idLogistica', 'ventapedidoId', 'transportista', 'costoEnvio', 'direccion')
    search_fields = ('ventapedidoId__nombresCliente', 'transportista__nombres', 'direccion')
    list_filter = ('transportista__estado',)

admin.site.register(transportistas, TransportistaAdmin)
admin.site.register(VentaPedido, VentaPedidoAdmin)
admin.site.register(logistica, LogisticaAdmin)






