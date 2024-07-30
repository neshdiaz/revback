from django.db import models


class Compra(models.Model):
    fecha = models.DateField()
    notas = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Foreign keys
    proveedor = models.CharField(max_length=128)
    plataformas = models.CharField(max_length=128)
