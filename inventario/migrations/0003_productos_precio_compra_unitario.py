# Generated by Django 5.1.7 on 2025-03-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_inventario_stock_maximo_inventario_stock_minimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='precio_compra_unitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
