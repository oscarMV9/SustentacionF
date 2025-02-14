from django.db import models
from produccion.models import Produccion
from Categorias.models import CategoriaColor, CategoriaGenero, CategoriaPrenda, CategoriaTalla
from django.core.exceptions import ValidationError

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Produccion, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_nombre_producto(self):
        return self.idProducto.nombreProducto

    def __str__(self):
        return self.idProducto.nombreProducto
    
  
class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidades = models.IntegerField()
    categoriaTalla = models.ForeignKey(CategoriaTalla,on_delete=models.CASCADE)
    categoriaColor = models.ForeignKey(CategoriaColor,on_delete=models.CASCADE)
    categoriaPrenda = models.ForeignKey(CategoriaPrenda,on_delete=models.CASCADE)
    categoriaGenero = models.ForeignKey(CategoriaGenero,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def clean(self):
        if self.cantidades < 0:
            raise ValidationError("la cantidad no puede ser negativo")
        
        if Inventario.objects.filter(
            idProducto=self.idProducto,
            categoriaTalla=self.categoriaTalla,
            categoriaColor=self.categoriaColor,
            categoriaPrenda=self.categoriaPrenda,
            categoriaGenero=self.categoriaGenero,
        ).exists():
            raise ValidationError("el registro ya existe en el inventario")
        
    def __str__(self):
        return f"{self.descripcion} - {self.idProducto.get_nombre_producto()} - {self.cantidades} unidades"


 
