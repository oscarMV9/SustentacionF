from django.db import models
from django.core.exceptions import ValidationError
from inventario.models import Inventario, Productos

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(null=False, max_length=50)
    apellido_cliente = models.CharField(null=False,max_length=50)
    cedula = models.CharField(null=False,max_length=20)
    correo = models.TextField(null=True, default="no brinda correo")
    direccion = models.TextField(null=True,default="000000")
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"venta de: {self.nombre_cliente} {self.apellido_cliente}, cedula {self.cedula}"
    
class VentaItem(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE,related_name="items")
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"producto: {self.producto.idProducto.get_nombre_producto} cantidades: {self.cantidad} de el pedido {self.venta.cedula}"