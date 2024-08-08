from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Equipo
from .serializers import EquipoSerializer

class EquipoViewSet(viewsets.ModelViewSet):
  queryset = Equipo.objects.all()
  serializer_class = EquipoSerializer
