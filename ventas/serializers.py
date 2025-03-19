from rest_framework import serializers
from .models import Venta, VentaItem

class VentaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaItem
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    items = VentaItemSerializer(many=True)

    class Meta:
        model = Venta
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items',[])
        venta = Venta.objects.create(**validated_data)

        for item_data in items_data:
            VentaItem.objects.create(venta=venta, **item_data)

        return venta