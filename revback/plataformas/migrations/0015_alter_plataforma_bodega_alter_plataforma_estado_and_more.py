# Generated by Django 5.0.7 on 2024-07-31 20:01

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodegas', '0003_remove_bodega_plataformas'),
        ('plataformas', '0014_alter_plataforma_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='bodega',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='plataformas_en_bodega', to='bodegas.bodega'),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='estado',
            field=models.CharField(choices=[('VEND ', 'Vendida'), ('VENC', 'Vencida'), ('ADQ ', 'Adquirida')], default='ADQ', max_length=5),
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
            name='fecha_compra',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2024, 8, 30, 20, 1, 8, 274761, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='url_imagen',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='vigencia',
            field=models.SmallIntegerField(default=30),
        ),
    ]
