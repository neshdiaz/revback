from rest_framework import serializers
from .models import Plataforma, TipoPlataforma
from bodegas.models import Bodega


class PlataformaSerializer(serializers.ModelSerializer):
    bodega = serializers.PrimaryKeyRelatedField(queryset=Bodega.objects.all())
    tipo = serializers.PrimaryKeyRelatedField(queryset=TipoPlataforma.objects.all())

    class Meta:
        model = Plataforma
        fields = [
            "correo",
            "contrasena",
            "estado",
            "estado_pago_proveedor",
            "fecha_pagada_proveedor",
            "estado_pago_vendedor",
            "fecha_pagada_vendedor",
            "fecha_compra",
            "fecha_vencimiento",
            "vigencia",
            "precio_compra",
            "precio_venta",
            "precio_venta_2",
            "notas",
            "bodega",
            "compra",
            "tipo",
        ]


class TipoPlataformaSerializer(serializers.ModelSerializer):
    plataformas_x_tipo_plataforma = PlataformaSerializer(many=True)

    class Meta:
        model = TipoPlataforma
        fields = [
            "nombre",
            "descripcion",
            "url_imagen",
            "precio_referencia",
            "plataformas_x_tipo_plataforma",
        ]
