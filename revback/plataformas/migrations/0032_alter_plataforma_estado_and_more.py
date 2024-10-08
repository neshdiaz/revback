# Generated by Django 5.0.7 on 2024-08-10 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformas', '0031_alter_plataforma_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='estado',
            field=models.CharField(choices=[('VENC', 'Vencida'), ('ADQ', 'Adquirida'), ('RENO', 'Renovada'), ('VEND', 'Vendida')], default='ADQ', max_length=5),
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
            field=models.DateField(default=datetime.datetime(2024, 9, 9, 16, 28, 11, 600507, tzinfo=datetime.timezone.utc)),
        ),
    ]
