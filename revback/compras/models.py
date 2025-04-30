from django.db import models
from proveedores.models import Proveedor

class Compra(models.Model):
    ESTADO_PAGO = {
        ("PAG", "Pagada"),
        ("P_PAG", "Pendiente Pago"),
    }

    fecha = models.DateField()
    notas = models.TextField(blank=True, null=True)
    estado_pago = models.CharField(
        max_length=5, choices=ESTADO_PAGO, default="P_PAG"
    )
    fecha_pago = models.DateField(null=True, blank=True)
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
 
class Compra_detalle (models.Model):
    Compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="compras_detalle")
    Plataforma = models.ForeignKey("plataformas.Plataforma", on_delete=models.PROTECT, related_name="compras_detalle")
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.created.date()) + "-" + str(self.id)

    class Meta:
        ordering = ["created"]