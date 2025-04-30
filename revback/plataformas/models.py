from django.db import models
from django.utils import timezone
from datetime import timedelta
from bodegas.models import Bodega
from compras.models import Compra


class TipoPlataforma(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    url_imagen = models.CharField(max_length=128, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["created"]


class Plataforma(models.Model):

    ESTADO_PLATAFORMA = {
        ("ADQ", "Adquirida"),
        ("VENC", "Vencida"),
        ("VEND", "Vendida"),
        ("RENO", "Renovada"),
    }

    correo = models.CharField(max_length=128, unique=True)
    contrasena = models.CharField(max_length=128)
    estado = models.CharField(max_length=5, choices=ESTADO_PLATAFORMA, default="ADQ")
    fecha_compra = models.DateField(default=timezone.now)
    fecha_vencimiento = models.DateField(default=timezone.now() + timedelta(days=30))
    vigencia = models.SmallIntegerField(default=30)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notas = models.TextField(null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # foreign keys
    bodega = models.ForeignKey(
        Bodega,
        on_delete=models.CASCADE,
        related_name="plataformas_en_la_bodega",
        default=1,
    )
    tipo = models.ForeignKey(
        TipoPlataforma,
        on_delete=models.CASCADE,
        related_name="plataformas_x_tipo_plataforma",
    )

    def __str__(self):
        return self.correo

    class Meta:
        ordering = ["created"]

class CaracteristicasPlataforma(models.Model):
    ESTADO_VENTA = {
        ("TOTAL", "Total"),
        ("PARCIAL", "Parcial"),
    }

    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    estado_venta = models.CharField(
        max_length=7, choices=ESTADO_VENTA, default="PARCIAL"
    )
    vendida = models.BooleanField(default=False)
    tipo_plataforma = models.ForeignKey(TipoPlataforma, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["created"]

class CaracteristicasPlataformaValor(models.Model):
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    caracteristica = models.ForeignKey(CaracteristicasPlataforma, on_delete=models.CASCADE)
    valor= models.CharField(max_length=128)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
