from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import Compra
from .serializers import CompraSerializer


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
