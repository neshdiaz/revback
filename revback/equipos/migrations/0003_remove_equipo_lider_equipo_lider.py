# Generated by Django 5.0.7 on 2024-07-30 21:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_equipo_lider_equipo_usuarios'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='lider',
        ),
        migrations.AddField(
            model_name='equipo',
            name='lider',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
