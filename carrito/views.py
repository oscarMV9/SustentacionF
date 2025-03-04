from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Orden, OrdenItem
from inventario.models import Inventario
import json
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        carrito = data.get('carrito')
        nombre_cliente = data.get('nombre_cliente')
        N_documento = data.get('N_documento')
        telefono = data.get('telefono')
        direccion = data.get('direccion')
        email = data.get('email')

        if not carrito or not nombre_cliente or not N_documento or not telefono or not direccion or not email:
            return JsonResponse({'error': 'Faltan datos necesarios'}, status=400)
        
        total = 0
        nueva_orden = Orden.objects.create(
            nombre_cliente=nombre_cliente,
            N_documento=N_documento,
            telefono=telefono,
            direccion=direccion,
            email=email,
            total=0
        )

        for item in carrito:
            producto = Inventario.objects.get(id=item['id'])
            OrdenItem.objects.create(
                orden=nueva_orden,
                producto=producto,
                cantidad=item['cantidad'],
                precio_unitario=item['precio']
            )
            producto.cantidades -= item['cantidad']
            producto.save()
            total += item['cantidad'] * item['precio']
        nueva_orden.total = total
        nueva_orden.save()

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, f"Recibo de Pedido #{nueva_orden.id}")
        p.drawString(100, 730, f"Cliente: {nueva_orden.nombre_cliente}")
        p.drawString(100, 710, f"Documento: {nueva_orden.N_documento}")
        p.drawString(100, 690, f"Teléfono: {nueva_orden.telefono}")
        p.drawString(100, 670, f"Dirección: {nueva_orden.direccion}")
        p.drawString(100, 650, f"Email: {nueva_orden.email}")
        p.drawString(100, 630, f"Fecha: {nueva_orden.fecha}")
        p.drawString(100, 610, "Productos:")
        y = 590
        for item in nueva_orden.items.all():
            p.drawString(100, y, f"{item.cantidad}x {item.producto.idProducto.get_nombre_producto()} - {item.precio_unitario} c/u")
            y -= 20
        p.drawString(100, y, f"Total: {nueva_orden.total}")
        p.showPage()
        p.save()

        buffer.seek(0)
        pdf = buffer.getvalue()
        buffer.close()

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="recibo_pedido_{nueva_orden.id}.pdf"'

        return response

    return JsonResponse({'error': 'Método no permitido'}, status=405)