from rest_framework import serializers
from .models import Venta, VentaItem

class VentaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaItem
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    items = VentaItemSerializer(many=True, read_only=True)

    class Meta:
        model = Venta
        fields = '__all__'