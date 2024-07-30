from django.db import models


class Plataforma(models.Model):

    ESTADO_PLATAFORMA = {
        ("ADQ ", "Adquirida"),
        ("VENC", "Vencida"),
        ("VEND ", "Vendida"),
    }

    ESTADO_PAGO = {
        ("PAG ", "Pagada"),
        ("P_PAG", "Pendiente Pago"),
    }

    correo = models.CharField(max_length=128)
    contraseña = models.CharField(max_length=128)
    estado = models.CharField(max_length=5, choices=ESTADO_PLATAFORMA)
    estado_pago_proveedor = models.CharField(max_length=5, choices=ESTADO_PAGO)
    fecha_pagada_proveedor = models.DateField()
    estado_pago_vendedor = models.CharField(max_length=5, choices=ESTADO_PAGO)
    fecha_pagada_vendedor = models.DateField()
    fecha_compra = models.DateField()
    fecha_vencimiento = models.DateField()
    vigencia = models.SmallIntegerField()
    costo_unitario_compra = models.DecimalField(max_digits=10, decimal_places=2)
    costo_unitario_venta = models.DecimalField(max_digits=10, decimal_places=2)
    costo_unitario_venta_esp_1 = models.DecimalField(max_digits=10, decimal_places=2)
    costo_unitario_venta_esp_2 = models.DecimalField(max_digits=10, decimal_places=2)
    url_imagen = models.CharField(max_length=128)
    notas = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # foreing keys
    tipo_plataforma = models.CharField(max_length=128)
    bodega_actual = models.CharField(max_length=128)
    compras = models.CharField(max_length=128)
    traslados = models.CharField(max_length=128)


class TipoPlataforma(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    url_imagen = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # foreing keys
    plataformas = models.ForeignKey(Plataforma, on_delete=models.DO_NOTHING)
