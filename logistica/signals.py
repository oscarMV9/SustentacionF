# from django.core.mail import send_mail
# from django.core.mail import BadHeaderError
# from django.core.exceptions import ValidationError
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Logistica

# @receiver(post_save, sender=Logistica)
# def enviarCorreoLogistica(sender, instance, created, **kwargs):
#     if created:
#         asunto = 'Nueva Orden pedida.'
#         mensaje = (f"Se ha solicitado un nuevo Domicilio. \n{instance.orden}. \n{instance.fecha}")
#         # destinatarios = ['jdbuitragob3@gmail.com']
#         destinatarios = ['davrip2005@gmail.com']

#         try:
#             send_mail(asunto, mensaje, 'anastylesgaes4@gmail.com', destinatarios)
#         except BadHeaderError:
#             raise ValidationError("Error en el encabezado del correo")
#         except Exception as e:
#             print(f"Ocurrió un error: {e}")

from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Logistica

@receiver(post_save, sender=Logistica)
def enviarCorreoLogistica(sender, instance, created, **kwargs):
    if created:
        asunto = 'Nueva Orden Pedida - Logística'

        productos = instance.get_productos()

        productos_html = ""
        for producto in productos:
            productos_html += f"""
            <p><strong>Producto:</strong> {producto['producto']}<br>
            <strong>Cantidad:</strong> {producto['cantidad']}<br>
            <strong>Precio unitario:</strong> {producto['precio_unitario']}<br>
            <strong>Total:</strong> {producto['total']}</p>
            <hr>
            """

        mensaje = f"""
        <html>
            <body>
                <h2>Se ha solicitado un nuevo Domicilio</h2>
                <p><strong>Orden:</strong> {instance.orden}</p>
                <p><strong>Fecha de Solicitud:</strong> {instance.fecha}</p>
                <h3>Productos en la Orden:</h3>
                {productos_html}
                <p>Este correo es generado automáticamente para notificar sobre la nueva orden de logística.</p>
            </body>
        </html>
        """

        destinatarios = ['jdbuitragob3@gmail.com']

        try:
            send_mail(
                asunto, 
                mensaje, 
                'anastylesgaes4@gmail.com', 
                destinatarios, 
                html_message=mensaje
            )
        except BadHeaderError:
            raise ValidationError("Error en el encabezado del correo")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
