# Generated by Django 5.0.7 on 2024-08-09 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_alter_compra_proveedor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={'ordering': ['created']},
        ),
    ]
