# Generated by Django 5.0.7 on 2024-08-12 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformas', '0032_alter_plataforma_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='estado',
            field=models.CharField(choices=[('ADQ', 'Adquirida'), ('VEND', 'Vendida'), ('RENO', 'Renovada'), ('VENC', 'Vencida')], default='ADQ', max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='estado_pago_proveedor',
            field=models.CharField(choices=[('P_PAG', 'Pendiente Pago'), ('PAG ', 'Pagada')], default='P_PAG', max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='estado_pago_vendedor',
            field=models.CharField(choices=[('P_PAG', 'Pendiente Pago'), ('PAG ', 'Pagada')], default='P_PAG', max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2024, 9, 11, 19, 33, 35, 316149, tzinfo=datetime.timezone.utc)),
        ),
    ]
