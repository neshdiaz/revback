# Generated by Django 5.0.7 on 2024-07-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=128)),
                ('apellidos', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('web', models.CharField(max_length=256)),
                ('whatsapp', models.CharField(max_length=128)),
                ('activo', models.BooleanField()),
                ('url_imagen', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('compras', models.CharField(max_length=128)),
            ],
        ),
    ]
