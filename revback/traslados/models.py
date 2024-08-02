from django.db import models
from usuarios.models import Usuario
from plataformas.models import Plataforma
from bodegas.models import Bodega


class Traslado(models.Model):
    fecha = models.DateField()
    notas = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Foreign keys
    responsable = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name="responsable_de_traslados",
    )
    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.PROTECT,
        related_name="traslados_realizados",
    )
    bodega_origen = models.ForeignKey(
        Bodega,
        on_delete=models.PROTECT,
        related_name="traslados_desde",
    )
    bodega_destino = models.ForeignKey(
        Bodega,
        on_delete=models.PROTECT,
        related_name="traslados_hacia",
    )
