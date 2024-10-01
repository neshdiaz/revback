from rest_framework import serializers
from django.contrib.auth.models import User
from usuarios.models import Usuario
from .models import Bodega

class usuarioAuthSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['first_name', 'last_name']

class UsuarioSerializer(serializers.ModelSerializer):
  usuario_auth = usuarioAuthSerializer(read_only=True)
  class Meta:
    model = Usuario
    fields = ['usuario_auth']

class BodegaSerializer(serializers.ModelSerializer):
  responsables = UsuarioSerializer(many=True, read_only=True)
  class Meta:
    model = Bodega
    fields = ['id', 'nombre', 'created', 'updated', 'responsables']

