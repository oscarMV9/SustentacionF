from django import forms
from .models import Produccion

class ProduccionForms(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['nombreProducto', 'nombreProveedor', 'cantidad', 'materiales', 'costoProduccion', 'fecha_finalizacion']