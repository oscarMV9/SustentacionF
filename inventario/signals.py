# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib import messages
# from inventario.models import Inventario

# @receiver(post_save, sender=Inventario)
# def alerta_stock_bajo(sender, instance, **kwargs):
#     """
#     Envía una alerta al Admin de Django si el stock es <= stock mínimo.
#     """
#     if instance.cantidades <= instance.stock_minimo:
#         print(f"⚠️ ALERTA: Stock bajo para {instance.idProducto} - {instance.cantidades} unidades (Mínimo: {instance.stock_minimo})")
