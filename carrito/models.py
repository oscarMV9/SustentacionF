from django.db import models
from inventario.models import Inventario
from django.core.exceptions import ValidationError
from django.db import transaction

class Orden(models.Model):
    nombre_cliente = models.CharField(max_length=255) 
    N_documento = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=20, default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden {self.id} - Cliente: {self.nombre_cliente} documento: {self.N_documento}"


class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.idProducto.get_nombre_producto()} - {self.precio_unitario} c/u"
