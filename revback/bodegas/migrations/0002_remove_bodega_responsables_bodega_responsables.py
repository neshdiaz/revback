# Generated by Django 5.0.7 on 2024-07-30 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodegas', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodega',
            name='responsables',
        ),
        migrations.AddField(
            model_name='bodega',
            name='responsables',
            field=models.ManyToManyField(to='usuarios.usuario'),
        ),
    ]
