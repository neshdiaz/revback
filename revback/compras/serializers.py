from rest_framework import serializers
from .models import Compra
from plataformas.models import Plataforma
from plataformas.serializers import PlataformaSerializer


class CompraSerializer(serializers.ModelSerializer):
    plataformas_en_compra = PlataformaSerializer(many=True)

    class Meta:
        model = Compra
        fields = ["fecha", "notas", "proveedor", "plataformas_en_compra"]

    def create(self, validated_data):
        plataformas_data = validated_data.pop("plataformas_en_compra")
        compra = Compra.objects.create(**validated_data)

        for plataforma_data in plataformas_data:
            Plataforma.objects.create(compra=compra, **plataforma_data)
        return
