from rest_framework import serializers
from .models import Traslado

class TrasladoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Traslado
    fields = '__all__'