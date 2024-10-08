# Generated by Django 5.0.7 on 2024-07-31 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformas', '0019_alter_plataforma_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='estado',
            field=models.CharField(choices=[('ADQ', 'Adquirida'), ('VENC', 'Vencida'), ('VEND', 'Vendida')], default='ADQ', max_length=5),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2024, 8, 30, 20, 5, 11, 186824, tzinfo=datetime.timezone.utc)),
        ),
    ]
