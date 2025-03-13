
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User  # Importación del modelo de usuario de Django

@receiver(post_save, sender=User)
def enviarCorreoBienvenida(sender, instance, created, **kwargs):
    if created:  # Verifica si es un nuevo usuario
        asunto = 'Bienvenido a nuestro sitio'
        mensaje = f'Hola {instance.username}, gracias por registrarte.'
        destinatarios = [instance.email]  # El correo del usuario registrado
        send_mail(asunto, mensaje, 'anastylesgaes4@gmail.com', destinatarios)
