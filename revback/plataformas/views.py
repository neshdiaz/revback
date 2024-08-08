from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Plataforma
from .serializers import PlataformaSerializer

class PlataformaViewSet(viewsets.ModelViewSet):
  queryset = Plataforma.objects.all()
  serializer_class = PlataformaSerializer
