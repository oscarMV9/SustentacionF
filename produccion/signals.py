# from django.core.mail import send_mail
# from django.core.mail import BadHeaderError
# from django.core.exceptions import ValidationError
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Produccion

# @receiver(post_save, sender=Produccion)
# def enviarCorreoNuevoProducto(sender, instance, created, **kwargs):
#     if created:
#         asunto = 'Nuevo producto solicitado'
#         mensaje = (f"Se ha agregado un nuevo producto:\n\nNombre: {instance.nombreProducto}\nDescripción: {instance.descripcion}\nProveedor: {instance.nombreProveedor}\nCantidad: {instance.cantidad}\nMateriales: {instance.materiales}\nCosto de producción: {instance.costoProduccion}\nFecha de finalización: {instance.fecha_finalizacion}")
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
from .models import Produccion

@receiver(post_save, sender=Produccion)
def enviarCorreoNuevoProducto(sender, instance, created, **kwargs):
    if created:
        # Asunto del correo
        asunto = 'Nuevo Producto Solicitado - Producción'

        # Mensaje con formato HTML
        mensaje = f"""
        <html>
            <body>
                <h2>Nuevo Producto Solicitado</h2>
                <p><strong>Nombre del Producto:</strong> {instance.nombreProducto}</p>
                <p><strong>Descripción:</strong> {instance.descripcion}</p>
                <p><strong>Proveedor:</strong> {instance.nombreProveedor}</p>
                <p><strong>Cantidad:</strong> {instance.cantidad}</p>
                <p><strong>Materiales:</strong> {instance.materiales}</p>
                <p><strong>Costo de Producción:</strong> ${instance.costoProduccion}</p>
                <p><strong>Fecha de Finalización:</strong> {instance.fecha_finalizacion}</p>
                <hr>
                <p>Este correo es generado automáticamente para notificar sobre el nuevo producto solicitado en producción.</p>
            </body>
        </html>
        """

        destinatarios = ['davrip2005@gmail.com']

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

