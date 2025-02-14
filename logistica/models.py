from django.db import models
from ventas.models import Clientes
from inventario.models import Productos,Inventario
from django.core.exceptions import ValidationError

ESTADOS = [
    ('DISPONIBLE','DISPONIBLE'),
    ('EN ENTREGA','EN ENTREGA'),
]

class transportistas(models.Model):
    idTransportista = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    telefono = models.CharField(max_length=10)
    estado = models.CharField(max_length=40, choices=ESTADOS)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.estado}"

class VentaPedido(models.Model):
    idVentaPedido = models.AutoField(primary_key=True)
    nombresCliente = models.CharField(max_length=25)
    apellidosCliente = models.CharField(max_length=25)
    inventario = models.ForeignKey(Inventario,on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fechaPedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    direccion = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if self.cantidad > self.inventario.cantidades:
            raise ValidationError("el inventario es insuficiente para las cantidades")
        
        self.total = self.cantidad * self.inventario.idProducto.precio

        self.inventario.cantidades -= self.cantidad
        self.inventario.save(*args, **kwargs)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"pedido de venta: {self.idVentaPedido} - cliente: {self.nombresCliente} - producto: {self.inventario.idProducto.get_nombre_producto}, total:{self.total}"


class logistica(models.Model):
    idLogistica = models.AutoField(primary_key=True)
    ventapedidoId = models.ForeignKey(VentaPedido,on_delete=models.CASCADE)
    costoEnvio = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    transportista = models.ForeignKey(transportistas, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.direccion = self.ventapedidoId.direccion

        if self.transportista.estado == 'EN ENTREGA':
            raise ValidationError("este transportista esta ocupado, seleccione otro porfavor")
        
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"entrega #{self.idLogistica} - venta{self.ventapedidoId.inventario.idProducto.get_nombre_producto}, costo de venta a pagar: {self.ventapedidoId.total}"
