# Generated by Django 4.2 on 2025-02-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_inventario_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='productos/'),
        ),
    ]
