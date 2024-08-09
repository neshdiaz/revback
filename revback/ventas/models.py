from django.db import models
from clientes.models import Cliente


class Venta(models.Model):
    fecha = models.DateField()
    notas = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Foreign keys
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name="ventas_del_cliente"
    )

    def __str__(self):
        return str(self.created.date()) + "-" + str(self.id)

    class Meta:
        ordering = ['created']
