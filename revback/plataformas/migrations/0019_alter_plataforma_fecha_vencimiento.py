# Generated by Django 5.0.7 on 2024-07-31 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataformas', '0018_alter_plataforma_estado_pago_proveedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2024, 8, 30, 20, 5, 1, 279427, tzinfo=datetime.timezone.utc)),
        ),
    ]
