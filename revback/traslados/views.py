from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Traslado
from .serializers import TrasladoSerializer

class TrasladoViewSet(viewsets.ModelViewSet):
  queryset = Traslado.objects.all()
  serializer_class = TrasladoSerializer
