from django.db import models
from clientes.models import Cliente


class Venta(models.Model):

    ESTADO_PAGO = {
        ("PAG", "Pagada"),
        ("P_PAG", "Pendiente Pago"),
    }

    fecha = models.DateField()
    notas = models.TextField()
    estado_pago = models.CharField(
        max_length=5, choices=ESTADO_PAGO, default="P_PAG"
    )
    fecha_pago = models.DateField(null=True, blank=True)
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
