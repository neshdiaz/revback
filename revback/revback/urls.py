"""
URL configuration for revback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from bodegas.views import BodegaViewSet
from clientes.views import ClienteViewSet
from compras.views import CompraViewSet
from equipos.views import EquipoViewSet
from plataformas.views import PlataformaViewSet, TipoPlataformaViewSet
from proveedores.views import ProveedorViewSet
from traslados.views import TrasladoViewSet
from usuarios.views import UsuarioViewSet
from ventas.views import VentaViewSet

router = routers.DefaultRouter()
router.register(r"bodegas", BodegaViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"compras", CompraViewSet)
router.register(r"equipos", EquipoViewSet)
router.register(r"plataformas", PlataformaViewSet)
router.register(r"tipo-plataformas", TipoPlataformaViewSet)
router.register(r"proveedores", ProveedorViewSet)
router.register(r"traslados", TrasladoViewSet)
router.register(r"usuarios", UsuarioViewSet)
router.register(r"ventas", VentaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))
]
