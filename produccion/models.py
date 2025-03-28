from django.core.exceptions import ValidationError
from django.db import models

class Produccion(models.Model):
    idProduccion = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=70, null=False)
    descripcion = models.CharField(max_length=250)
    nombreProveedor = models.CharField(max_length=70)
    cantidad = models.IntegerField(null=False)
    materiales = models.CharField(max_length=70)
    costoProduccion = models.DecimalField(max_digits=23,decimal_places=2)
    fecha_finalizacion = models.DateField()

    def clean(self):
        if Produccion.objects.filter(
            nombreProducto = self.nombreProducto,
        ).exists():
            raise ValidationError("ya hay un registro con estas mismas caracteristicas")


    def get_nombre_proveedor(self):
        return self.nombreProveedor

    def __str__(self):
        return f"{self.nombreProducto}"