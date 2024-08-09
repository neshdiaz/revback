from django.db import models
from usuarios.models import Usuario


class Bodega(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField
    principal = models.BooleanField
    activa = models.BooleanField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Foreign keys
    responsables = models.ManyToManyField(Usuario)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['created']
