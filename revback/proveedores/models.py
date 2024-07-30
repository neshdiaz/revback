from django.db import models


class Proveedor(models.Model):
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)
    web = models.CharField(max_length=256)
    whatsapp = models.CharField(max_length=128)
    activo = models.BooleanField()
    url_imagen = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Foreign keys
    compras = models.CharField(max_length=128)
