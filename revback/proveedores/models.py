from django.db import models
from usuarios.models import Usuario


class Proveedor(models.Model):
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True)
    web = models.CharField(max_length=256, null=True, blank=True)
    whatsapp = models.CharField(max_length=128, null=True, blank=True)
    url_imagen = models.CharField(max_length=256, null=True, blank=True)
    activo = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombres + " " + self.apellidos

    class Meta:
        verbose_name_plural = "Proveedores"
        ordering = ["created"]

