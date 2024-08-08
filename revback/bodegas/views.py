from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Bodega
from .serializers import BodegaSerializer

class BodegaViewSet(viewsets.ModelViewSet):
  queryset = Bodega.objects.all()
  serializer_class = BodegaSerializer