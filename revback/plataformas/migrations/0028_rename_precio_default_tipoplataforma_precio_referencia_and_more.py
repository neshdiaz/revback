# Generated by Django 5.0.7 on 2024-08-06 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformas', '0027_rename_costo_unitario_compra_plataforma_precio_compra_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipoplataforma',
            old_name='precio_default',
            new_name='precio_referencia',
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='estado',
            field=models.CharField(choices=[('VEND', 'Vendida'), ('RENO', 'Renovada'), ('VENC', 'Vencida'), ('ADQ', 'Adquirida')], default='ADQ', max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='estado_pago_proveedor',
            field=models.CharField(choices=[('PAG ', 'Pagada'), ('P_PAG', 'Pendiente Pago')], default='P_PAG', max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='estado_pago_vendedor',
            field=models.CharField(choices=[('PAG ', 'Pagada'), ('P_PAG', 'Pendiente Pago')], default='P_PAG', max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2024, 9, 5, 20, 36, 53, 440377, tzinfo=datetime.timezone.utc)),
        ),
    ]
