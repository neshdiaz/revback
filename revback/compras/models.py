from django.db import models
from proveedores.models import Proveedor


class Compra(models.Model):
    fecha = models.DateField()
    notas = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Foreign keys
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.PROTECT, related_name="compras_del_proveedor"
    )

    def __str__(self):
        return str(self.created.date()) + "-" + str(self.id)

    class Meta:
        ordering = ["created"]
