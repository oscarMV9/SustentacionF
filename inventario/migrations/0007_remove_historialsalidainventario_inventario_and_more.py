# Generated by Django 4.2 on 2025-03-28 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_historialsalidainventario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historialsalidainventario',
            name='inventario',
        ),
        migrations.DeleteModel(
            name='HistorialEntradaInventario',
        ),
        migrations.DeleteModel(
            name='HistorialSalidaInventario',
        ),
    ]
