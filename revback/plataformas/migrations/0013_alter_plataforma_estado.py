# Generated by Django 5.0.7 on 2024-07-31 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformas', '0012_alter_plataforma_estado_pago_proveedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='estado',
            field=models.CharField(choices=[('VEND ', 'Vendida'), ('ADQ ', 'Adquirida'), ('VENC', 'Vencida')], default='ADQ', max_length=5),
        ),
    ]
