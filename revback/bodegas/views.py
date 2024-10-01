from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Bodega
from .serializers import BodegaSerializer

class BodegaListView(generics.ListAPIView):
  queryset = Bodega.objects.all()
  serializer_class = BodegaSerializer