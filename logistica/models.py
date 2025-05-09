from django.db import models
from carrito.models import Orden, OrdenItem
from inventario.models import Inventario
from django.utils import timezone
from django.core.exceptions import ValidationError

ESTADOS = [
    ('DISPONIBLE', 'DISPONIBLE'),
    ('EN ENTREGA', 'EN ENTREGA'),
]

class Transportista(models.Model):
    idTransportista = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    telefono = models.CharField(max_length=10)
    estado = models.CharField(max_length=40, choices=ESTADOS)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.estado}"

class Logistica(models.Model):
    idLogistica = models.AutoField(primary_key=True)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE)
    costoEnvio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    direccion = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def get_productos(self):
        orden_items = self.orden.items.all()
        productos = []
        for item in orden_items:
            producto = item.producto
            productos.append({
                'producto': producto.idProducto.get_nombre_producto(),
                'cantidad': item.cantidad,
                'precio_unitario': item.precio_unitario,
                'total': item.cantidad * item.precio_unitario
            })
        return productos

    def save(self, *args, **kwargs):
        self.direccion = self.orden.direccion

        if self.transportista.estado == 'EN ENTREGA':
            raise ValidationError("Este transportista se encuentra ocupado, seleccione otro por favor.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Entrega #{self.idLogistica} - Orden {self.orden.id}, Costo de envío: {self.costoEnvio}"
