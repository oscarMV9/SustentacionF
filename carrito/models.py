from django.db import models
from inventario.models import Inventario
from django.core.exceptions import ValidationError
from django.db import transaction

class Carrito(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    horaCreacion = models.DateTimeField(auto_now_add=True)

    def procesar_compra(self, nombre_cliente, telefono, direccion):
        with transaction.atomic():
            if not CarritoItem.objects.filter(carrito=self).exists():
                raise ValidationError("El carrito está vacío. Agrega productos antes de procesar la compra.")

            total = 0
            nueva_orden = Orden.objects.create(
                nombre_cliente=nombre_cliente,
                telefono=telefono,
                direccion=direccion,
                total=0
            )

            for item in CarritoItem.objects.filter(carrito=self):
                if item.cantidad > item.producto.cantidades:
                    raise ValidationError(f"No hay suficiente stock para {item.producto.idProducto.get_nombre_producto()}.")

                item.producto.cantidades -= item.cantidad
                item.producto.save()

                OrdenItem.objects.create(
                    orden=nueva_orden,
                    producto=item.producto,
                    cantidad=item.cantidad,
                    precio_unitario=item.producto.idProducto.precio
                )

                total += item.cantidad * item.producto.idProducto.precio

            nueva_orden.total = total
            nueva_orden.save()

            CarritoItem.objects.filter(carrito=self).delete()

    def __str__(self):
        return f"Carrito de sesión {self.session_id}"


class Orden(models.Model):
    nombre_cliente = models.CharField(max_length=255) 
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden {self.id} - Cliente: {self.nombre_cliente}"


class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.idProducto.get_nombre_producto()} - {self.precio_unitario} c/u"


class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def clean(self):
        if self.cantidad > self.producto.cantidades:
            raise ValidationError("No hay suficiente stock disponible para este producto.")

    def __str__(self):
        return f"{self.producto.idProducto.get_nombre_producto()} - {self.cantidad} unidades"
