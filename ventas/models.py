from django.db import models
from django.core.exceptions import ValidationError
from inventario.models import Inventario, Productos
from django.db.models import F
from django.db import transaction

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(null=False, max_length=50)
    apellido_cliente = models.CharField(null=False,max_length=50)
    cedula = models.CharField(null=False,max_length=20)
    correo = models.TextField(null=True, default="no brinda correo")
    direccion = models.TextField(null=True, default="000000")
    fecha = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        return f"venta de: {self.nombre_cliente} {self.apellido_cliente}, cedula {self.cedula}"

class VentaItem(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad

    def save(self, *args, **kwargs):
        if self.cantidad > self.producto.cantidades:
            raise ValidationError("No hay suficiente cantidad en inventario para este producto.")
        
        with transaction.atomic():
            self.producto.cantidades = F('cantidades') - self.cantidad
            self.producto.save()
            super().save(*args, **kwargs)

    def __str__(self):
        return f"producto: {self.producto.idProducto.get_nombre_producto()} cantidad: {self.cantidad} de la venta {self.venta.cedula}"

