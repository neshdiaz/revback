# Generated by Django 5.0.7 on 2024-07-31 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0004_remove_equipo_lider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='usuarios',
        ),
    ]
