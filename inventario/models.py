from django.db import models
from produccion.models import Produccion
from Categorias.models import CategoriaColor, CategoriaGenero, CategoriaPrenda, CategoriaTalla
from django.core.exceptions import ValidationError


class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Produccion, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=False)
    descripcion = models.CharField(max_length=100)
    precio_compra_unitario_de_fabrica = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_nombre_producto(self):
        return self.idProducto.nombreProducto

    def __str__(self):
        return self.idProducto.nombreProducto

    def formatear_precio(self):
        return f"${self.precio:.2f}"

  
class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidades = models.IntegerField()
    stock_minimo = models.IntegerField(default=10)
    stock_maximo = models.IntegerField(default=500)
    categoriaTalla = models.ForeignKey(CategoriaTalla,on_delete=models.CASCADE)
    categoriaColor = models.ForeignKey(CategoriaColor,on_delete=models.CASCADE)
    categoriaPrenda = models.ForeignKey(CategoriaPrenda,on_delete=models.CASCADE)
    categoriaGenero = models.ForeignKey(CategoriaGenero,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def clean(self):
        if self.cantidades < 0:
            raise ValidationError("la cantidad no puede ser negativo")

        if self.cantidades < self.stock_minimo:
            raise ValidationError("la cantidad no puede ser menor al stock minimo")
        
        if self.cantidades > self.stock_maximo:
            raise ValidationError("la cantidad no puede ser mayor al stock maximo")
        
        if Inventario.objects.filter(
            idProducto=self.idProducto,
            categoriaTalla=self.categoriaTalla,
            categoriaColor=self.categoriaColor,
            categoriaPrenda=self.categoriaPrenda,
            categoriaGenero=self.categoriaGenero,
        ).exclude(id=self.id).exists():
            raise ValidationError("el registro ya existe en el inventario")
 
    def precio_de_venta(self):
        return self.idProducto.precio
    
    
    def nombre_proveedor(self):
        return self.idProducto.idProducto.get_nombre_proveedor()

    def precio_de_fabrica(self):
        return self.idProducto.precio_compra_unitario_de_fabrica
    
    def ganancias_totales(self):
        return self.precio_de_venta() - self.precio_de_fabrica()
        
    def __str__(self):
        return f"{self.descripcion} - {self.idProducto.get_nombre_producto()} - {self.cantidades} unidades"
 
