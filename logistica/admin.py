from django.contrib import admin
from .models import Transportista, Logistica

@admin.register(Transportista)
class TransportistaAdmin(admin.ModelAdmin):
    list_display = ('idTransportista', 'nombres', 'apellidos', 'telefono', 'estado')
    search_fields = ('nombres', 'apellidos', 'telefono')
    list_filter = ('estado',)

@admin.register(Logistica)
class LogisticaAdmin(admin.ModelAdmin):
    list_display = ('idLogistica', 'orden', 'transportista', 'costoEnvio', 'direccion')
    search_fields = ('orden__id', 'transportista__nombres', 'transportista__apellidos')
    list_filter = ('transportista__estado',)