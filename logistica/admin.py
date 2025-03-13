from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Transportista, Logistica
from import_export import resources
from import_export.admin import ImportExportModelAdmin

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
        textObject.setFont("Helvetica-Bold", 12)
        
        textObject.textLine(f"ID Logística: {logistica.idLogistica}")
        textObject.setFont("Helvetica", 12)
        textObject.textLine(f"Transportista: {logistica.transportista.nombres} {logistica.transportista.apellidos}")
        textObject.textLine(f"Costo Envío: {logistica.costoEnvio}")
        textObject.textLine(f"Dirección: {logistica.direccion}")
        textObject.textLine("="*50)

    c.drawText(textObject)
    c.showPage()
    c.save()
    return response

GeneratePDFLogistica.short_description = "Generar reporte PDF de Logistica"

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


class LogisticaResource(resources.ModelResource):
    class Meta:
        model = Logistica
        fields = ('idLogistica', 'costoEnvio', 'transportista', 'direccion')

from .models import Transportista, Logistica


@admin.register(Transportista)
class TransportistaAdmin(admin.ModelAdmin):
    list_display = ('idTransportista', 'nombres', 'apellidos', 'telefono', 'estado')
    search_fields = ('nombres', 'apellidos', 'telefono')
    list_filter = ('estado',)
    actions = [GeneratePDFTransportista]

class LogisticaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LogisticaResource
    list_display = ('idLogistica', 'transportista', 'costoEnvio', 'direccion')
    search_fields = ('transportista__nombres', 'direccion')
    list_filter = ('transportista__estado',)
    actions = [GeneratePDFLogistica]
    
admin.site.register(Logistica, LogisticaAdmin)