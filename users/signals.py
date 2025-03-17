from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def enviarCorreoBienvenida(sender, instance, created, **kwargs):
    if created:
        asunto = 'Bienvenido a AnaStyles'
        destinatarios = [instance.email]
        
        # Contenido HTML del correo
        html_contenido = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bienvenido a AnaStyles</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #ffffff;
                    margin: 0;
                    padding: 0;
                    color: #333333;
                }}

                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    padding: 30px;
                    box-sizing: border-box;
                }}

                h2 {{
                    color: #111111;
                    font-size: 24px;
                    margin-bottom: 20px;
                }}

                p {{
                    color: #555555;
                    font-size: 16px;
                    line-height: 1.5;
                }}

                ul {{
                    color: #555555;
                    list-style-type: disc;
                    padding-left: 20px;
                }}

                .footer {{
                    margin-top: 30px;
                    text-align: center;
                    color: #888888;
                    font-size: 12px;
                }}

                .highlight {{
                    color: #000000;
                    font-weight: bold;
                }}

                .cta {{
                    margin-top: 20px;
                    text-align: center;
                    font-size: 18px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>¡Bienvenido a AnaStyles, {instance.username}!</h2>
                <p>Gracias por registrarte en nuestro sitio. Ahora podrás disfrutar de todos nuestros servicios y beneficios:</p>
                <ul>
                    <li>Consultar los productos que mas te gusten.</li>
                    <li>Comprar productos en línea con facilidad.</li>
                    <li>Recibir productos con garantia.</li>
                </ul>
                <p>Estamos felices de que formes parte de nuestra comunidad. Esperamos que disfrutes de la experiencia de compra en AnaStyles.</p>

                <div class="cta">
                    <p><a href="https://www.anastyles.com" style="color: #000000; text-decoration: none;">Visita nuestra tienda</a></p>
                </div>

                <div class="footer">
                    <p>Este es un correo automatizado. Por favor, no respondas a este mensaje.</p>
                </div>
            </div>
        </body>
        </html>
        """

        # Crear el objeto EmailMessage
        email = EmailMessage(
            asunto,
            html_contenido,
            'anastylesgaes4@gmail.com',  # Remitente
            destinatarios,
        )
        email.content_subtype = "html"  # Importante: establecer el tipo de contenido a HTML
        email.send()

