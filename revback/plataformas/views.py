from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Plataforma, TipoPlataforma
from .serializers import PlataformaSerializer, TipoPlataformaSerializer

class PlataformaViewSet(viewsets.ModelViewSet):
  queryset = Plataforma.objects.all()
  serializer_class = PlataformaSerializer

class TipoPlataformaViewSet(viewsets.ModelViewSet):
  queryset = TipoPlataforma.objects.all()
  serializer_class = TipoPlataformaSerializer
