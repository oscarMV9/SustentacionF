from django.db import models
from django.core.exceptions import ValidationError

class CategoriaGenero(models.Model):
    idCategoriaG = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=30)

    def __str__(self):
        return self.genero

class CategoriaPrenda(models.Model):
    idCategoriaP = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreCategoria

class CategoriaTalla(models.Model):
    idCategoriaT = models.AutoField(primary_key=True)
    tipoTalla = models.CharField(max_length=40)
    talla = models.CharField(max_length=12)

    def clean(self):
        calzado_tallas = [str(i) for i in range(34, 49)] 
        tallas_prenda = ['S', 'M', 'L', 'XL', 'XS', 'UNICA', 'BEBES 0-3 M', 'BEBES 3-6 M', 'BEBES 6-9 M', 'BEBES 9-12 M', 'BEBES 12-18', 'BEBES 18-24 M', 'BEBES 24-36 M'] 

        if self.tipoTalla == 'CALZADO' and self.talla not in calzado_tallas:
            raise ValidationError("La talla no es válida según el tipo de prenda [Calzado].")
        elif self.tipoTalla == 'PRENDA' and self.talla not in tallas_prenda:
            raise ValidationError("La talla no corresponde al tipo de prenda [Prendas].")
        
    def __str__(self):
        return f"{self.tipoTalla} - {self.talla}"

class CategoriaColor(models.Model):
    idCategoriaC = models.AutoField(primary_key=True)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color

