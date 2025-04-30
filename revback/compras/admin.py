from django.contrib import admin
from compras.models import Compra, Compra_detalle
from plataformas.models import Plataforma

class CompraDetalleInLine(admin.TabularInline):
  model = Compra_detalle
  extra = 0


class CompraAdmin(admin.ModelAdmin):
  inlines = [CompraDetalleInLine]  


admin.site.register(Compra, CompraAdmin)

