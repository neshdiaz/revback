from django.contrib import admin
from compras.models import Compra
from plataformas.models import Plataforma

class PlataformaInLine(admin.TabularInline):
  model = Plataforma
  extra = 0

class CompraAdmin(admin.ModelAdmin):
  inlines = [PlataformaInLine]  


admin.site.register(Compra, CompraAdmin)

