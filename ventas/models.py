from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Sum
from inventario.models import Inventario,Productos

class Clientes(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, null=False)
    apellido = models.CharField(max_length=70)
    email = models.EmailField(unique=True, null=False)
    telefono = models.CharField(max_length=15, null=True,blank=True)
    direccion = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name="pedidos")
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fechaPedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if self.cantidad > self.inventario.cantidades:
            raise ValidationError("inventario insuficiente para la cantidad")
        
        self.total = self.cantidad * self.inventario.idProducto.precio

        self.inventario.cantidades -= self.cantidad
        self.inventario.save(*args, **kwargs)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"detalle #{self.idVenta} - {self.inventario.idProducto.get_nombre_producto()} - cantidades: {self.cantidad}"

    