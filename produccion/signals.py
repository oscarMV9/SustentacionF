from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Produccion

@receiver(post_save, sender=Produccion)
def enviarCorreoNuevoProducto(sender, instance, created, **kwargs):
    if created:
        asunto = 'Nuevo producto solicitado'
        mensaje = (f"Se ha agregado un nuevo producto:\n\nNombre: {instance.nombreProducto}\nDescripción: {instance.descripcion}\nProveedor: {instance.nombreProveedor}\nCantidad: {instance.cantidad}\nMateriales: {instance.materiales}\nCosto de producción: {instance.costoProduccion}\nFecha de finalización: {instance.fecha_finalizacion}")
        destinatarios = ['oscarmontoya119@gmail.com']

        try:
            send_mail(asunto, mensaje, 'anastylesgaes4@gmail.com', destinatarios)
        except BadHeaderError:
            raise ValidationError("Error en el encabezado del correo")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
