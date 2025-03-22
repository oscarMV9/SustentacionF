from rest_framework import serializers
from .models import Venta, VentaItem

class VentaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaItem
        fields = ['producto', 'cantidad', 'precio_unitario']
        extra_kwargs = {
            'venta': {'required': False}
        }

class VentaSerializer(serializers.ModelSerializer):
    items = VentaItemSerializer(many=True)

    class Meta:
        model = Venta
        fields = ['nombre_cliente', 'apellido_cliente', 'cedula', 'correo', 'direccion', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        venta = Venta.objects.create(**validated_data)
        for item_data in items_data:
            VentaItem.objects.create(venta=venta, **item_data)
        return venta

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.nombre_cliente = validated_data.get('nombre_cliente', instance.nombre_cliente)
        instance.apellido_cliente = validated_data.get('apellido_cliente', instance.apellido_cliente)
        instance.cedula = validated_data.get('cedula', instance.cedula)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.save()

        # Actualizar los items
        keep_items = []
        for item_data in items_data:
            if "id" in item_data.keys():
                if VentaItem.objects.filter(id=item_data["id"]).exists():
                    item = VentaItem.objects.get(id=item_data["id"])
                    item.producto = item_data.get('producto', item.producto)
                    item.cantidad = item_data.get('cantidad', item.cantidad)
                    item.precio_unitario = item_data.get('precio_unitario', item.precio_unitario)
                    item.save()
                    keep_items.append(item.id)
                else:
                    continue
            else:
                item = VentaItem.objects.create(venta=instance, **item_data)
                keep_items.append(item.id)

        for item in instance.items.all():
            if item.id not in keep_items:
                item.delete()

        return instance