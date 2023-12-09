# Generated by Django 4.2.7 on 2023-12-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_producto_foto1_alter_producto_foto2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, help_text='Precio del producto en mangos', max_digits=6),
        ),
    ]
