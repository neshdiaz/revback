# Generated by Django 5.0.7 on 2024-07-31 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformas', '0007_remove_plataforma_tipo_plataforma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='estado',
            field=models.CharField(choices=[('VENC', 'Vencida'), ('VEND ', 'Vendida'), ('ADQ ', 'Adquirida')], max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='estado_pago_proveedor',
            field=models.CharField(choices=[('P_PAG', 'Pendiente Pago'), ('PAG ', 'Pagada')], max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='estado_pago_vendedor',
            field=models.CharField(choices=[('P_PAG', 'Pendiente Pago'), ('PAG ', 'Pagada')], max_length=5),
        ),
    ]
