from django.core.mail import BadHeaderError
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Venta, VentaItem
from django.db import transaction

@receiver(post_save, sender=Venta)
def enviarCorreoVenta(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: _enviar_correo_con_items(instance))

def _enviar_correo_con_items(instance):
    if not instance.items.exists():
        print("No hay items asociados a esta venta aún")
        return

    asunto = 'Tu recibo de Compra - Anastyles'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.setFont("Helvetica", 10)
    p.drawString(100, 750, f"Recibo de Compra - {instance.nombre_cliente} {instance.apellido_cliente}")
    p.drawString(100, 730, f"Cédula: {instance.cedula}")
    p.drawString(100, 710, f"Dirección: {instance.direccion}")
    p.drawString(100, 690, f"Fecha de Compra: {instance.fecha.strftime('%Y-%m-%d %H:%M:%S')}")
    p.drawString(100, 670, f"Total: ${instance.total:.2f}")

    p.setFont("Helvetica-Bold", 10)
    p.drawString(100, 640, "Productos Comprados:")
    
    y_position = 620
    p.setFont("Helvetica", 10)
    for item in instance.items.all():
        p.drawString(100, y_position, f"Producto: {item.producto.idProducto.get_nombre_producto()} - Cantidad: {item.cantidad} - Precio Unitario: ${item.precio_unitario:.2f} - Subtotal: ${item.subtotal:.2f}")
        y_position -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    productos_html = ""
    for item in instance.items.all():
        productos_html += f"""
        <div style="margin-bottom: 10px; padding: 8px; border-radius: 5px; background-color: #f8f8f8;">
            <p><strong>Producto:</strong> {item.producto.idProducto.get_nombre_producto()}</p>
            <p><strong>Cantidad:</strong> {item.cantidad}</p>
            <p><strong>Precio Unitario:</strong> ${item.precio_unitario:.2f}</p>
            <p><strong>Subtotal:</strong> ${item.subtotal:.2f}</p>
        </div>
        """

    mensaje = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recibo de Compra</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            .container {{
                width: 90%;
                max-width: 600px;
                margin: 30px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }}
            h2 {{
                text-align: center;
                color: #333;
                font-size: 22px;
                margin-bottom: 20px;
            }}
            p {{
                font-size: 16px;
                line-height: 1.5;
                color: #333;
            }}
            p strong {{
                font-weight: bold;
            }}
            .total {{
                margin-top: 20px;
                font-size: 18px;
                font-weight: bold;
                text-align: right;
                color: #2e7d32;
            }}
            .footer {{
                text-align: center;
                margin-top: 30px;
                font-size: 12px;
                color: #888;
            }}
            .product-item {{
                margin-bottom: 15px;
                padding: 12px;
                background-color: #f9f9f9;
                border-radius: 5px;
                box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Recibo de Compra</h2>
            <p><strong>Cliente:</strong> {instance.nombre_cliente} {instance.apellido_cliente}</p>
            <p><strong>Cédula:</strong> {instance.cedula}</p>
            <p><strong>Dirección:</strong> {instance.direccion}</p>
            <p><strong>Fecha de Compra:</strong> {instance.fecha.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p class="total"><strong>Total:</strong> ${instance.total:.2f}</p>
            
            <h3>Productos Comprados</h3>
            {productos_html}

            <div class="footer">
                <p>Gracias por tu compra. ¡Vuelve pronto!</p>
            </div>
        </div>
    </body>
    </html>
    """

    destinatarios = [instance.correo] if instance.correo != "no brinda correo" else []
    if not destinatarios:
        print("No hay correo destinatario para enviar el recibo")
        return

    email = EmailMultiAlternatives( 
        asunto,
        "Recibo de compra",
        'anastylesgaes4@gmail.com', 
        destinatarios,
    )

    email.attach_alternative(mensaje, "text/html")
    email.attach('recibo_compra.pdf', buffer.read(), 'application/pdf')

    try:
        email.send()
    except BadHeaderError:
        raise ValidationError("Error en el encabezado del correo")
    except Exception as e:
        print(f"Ocurrió un error al enviar el correo: {e}")

