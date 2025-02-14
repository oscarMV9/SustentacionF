from django.db import models
from django.core.exceptions import ValidationError

GENEROS = [
    ('HOMBRE','HOMBRE'),
    ('MUJER','MUJER'),
    ('NIÑO','NIÑO'),
    ('NIÑA','NIÑA'),
]

PRENDAS = [
    ('CAMISETAS','CAMISETAS'),
    ('CAMISAS','CAMISAS'),
    ('CHAQUETAS','CHAQUETAS'),
    ('PANTALONES','PANTALONES'),
    ('MEDIAS','MEDIAS'),
    ('SACOS','SACOS'),
    ('GUANTES', 'GUANTES'),
]

TIPTALLA = [
    ('CALZADO','CALZADO'),
    ('PRENDA','PRENDA'),
]

CALZADO = [
    ('34','34'),
    ('25','35'),
    ('36','36'),
    ('37','37'),
    ('38','38'),
    ('39','39'),
    ('40','40'),
    ('41','41'),
    ('42','42'),
    ('43','43'),
    ('44','44'),
    ('45','45'),
    ('46','46'),
    ('47','47'),
    ('48','48'),
]

TALLAS = [
    ('S','S'),
    ('M','M'),
    ('L','L'),
    ('XL','XL'),
    ('XS','XS'),
    ('UNICA','UNICA'),
]

class CategoriaPrenda(models.Model):
    idCategoriaP = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20, choices=PRENDAS)

    def __str__(self):
        return self.nombreCategoria

class CategoriaGenero(models.Model):
    idCategoriaG = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=30, choices=GENEROS)

    def __str__(self):
        return self.genero

class CategoriaTalla(models.Model):
    idCategoriaT = models.AutoField(primary_key=True)
    tipoTalla = models.CharField(max_length=40,choices=TIPTALLA)
    talla = models.CharField(max_length=12)

    def clean(self):
        if self.tipoTalla == 'CALZADO' and self.talla not in dict(CALZADO).keys():
            raise ValidationError("la talla no es valida segun el tipo de prenda [Calzado]")
        elif self.tipoTalla == 'PRENDA' and self.talla not in dict(TALLAS).keys():
            raise ValidationError("la talla no corresponde al tipo de prenda [Predas]")
        
    
    def _str_(self):
        return self.talla
    
COLOR = [
    ('ROJO','ROJO'),
    ('AZUL','AZUL'),
    ('AMARILLO','AMARILLO'),
    ('VINOTINTO','VINOTINTO'),
    ('BEIGE','BEIGE'),
    ('MORADO','MORADO'),
    ('VERDE','VERDE'),
    ('LIMA','LIMA'),
    ('CAFE','CAFE'),
    ('AZULREY','AZULREY'),
    ('GRIS','GRIS'),
    ('NEGRO','NEGRO'),
]
    
class CategoriaColor(models.Model):
    idCategoriaC = models.AutoField(primary_key=True)
    color = models.CharField(max_length=20, choices=COLOR)

    def _str_(self):
        return self.color

