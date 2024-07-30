from django.db import models


class Traslado(models.Model):
    fecha = models.DateField()
    notas = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Foreign keys
    responsable = models.CharField(max_length=128)
    plataforma = models.CharField(max_length=128)
    bodega_origen = models.CharField(max_length=128)
    bodega_destino = models.CharField(max_length=128)
