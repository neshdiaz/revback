from django.db import models
from django.utils import timezone
from datetime import timedelta
from bodegas.models import Bodega
from compras.models import Compra


class TipoPlataforma(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    url_imagen = models.CharField(max_length=128, null=True, blank=True)
    precio_default = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Plataforma(models.Model):

    ESTADO_PLATAFORMA = {
        ("ADQ", "Adquirida"),
        ("VENC", "Vencida"),
        ("VEND", "Vendida"),
        ("RENO", "Renovada"),
    }

    ESTADO_PAGO = {
        ("PAG ", "Pagada"),
        ("P_PAG", "Pendiente Pago"),
    }

    correo = models.CharField(max_length=128, unique=True)
    contraseña = models.CharField(max_length=128)
    estado = models.CharField(max_length=5, choices=ESTADO_PLATAFORMA, default="ADQ")
    estado_pago_proveedor = models.CharField(
        max_length=5, choices=ESTADO_PAGO, default="P_PAG"
    )
    fecha_pagada_proveedor = models.DateField(null=True, blank=True)
    estado_pago_vendedor = models.CharField(
        max_length=5, choices=ESTADO_PAGO, default="P_PAG"
    )
    fecha_pagada_vendedor = models.DateField(null=True, blank=True)
    fecha_compra = models.DateField(default=timezone.now)
    fecha_vencimiento = models.DateField(default=timezone.now() + timedelta(days=30))
    vigencia = models.SmallIntegerField(default=30)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    precio_venta_2 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    notas = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # foreign keys
    bodega = models.ForeignKey(
        Bodega,
        on_delete=models.PROTECT,
        related_name="plataformas_en_bodega",
        default=1,
    )
    compras = models.ForeignKey(
        Compra,
        on_delete=models.PROTECT,
        related_name="plataformas_en_compra",
        null=True,
        blank=True,
    )
    tipo = models.ForeignKey(
        TipoPlataforma,
        on_delete=models.PROTECT,
        related_name="plataformas_x_tipo_plataforma",
    )

    def __str__(self):
        return self.correo
