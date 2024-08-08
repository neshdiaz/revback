from rest_framework import serializers
from .models import Plataforma, TipoPlataforma

class PlataformaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Plataforma
    fields = '__all__'

class TipoPlataformaSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoPlataforma
    fields = '__all__'