from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from .models import Venta,Clientes


def render_to_pdf(template_name, context_dict={}):
    template = get_template(template_name)
    html = template.render(context_dict)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="venta.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    
    return response


def generar_pdf_admin(modeladmin, request, queryset):
    for venta in queryset:
        context = {
            'venta': venta,
            'cliente': venta.cliente,
        }
        response = render_to_pdf('venta_pdf.html', context)
        return response

@admin.register(Venta)
class VentasAdmin(ImportExportModelAdmin):
    list_display = ('idVenta','cliente',)
    search_fields = ('cliente',)
    actions = [generar_pdf_admin]

@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('idCliente', 'nombre',)
    search_fields = ('idClinte',)
