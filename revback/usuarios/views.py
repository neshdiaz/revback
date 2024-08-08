from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer
