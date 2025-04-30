from django.contrib import admin, messages
from bodegas.models import Bodega
from plataformas.models import Plataforma

class PlataformaStackedInLine(admin.StackedInline):
    model = Plataforma
    extra = 0

class BodegaAdmin(admin.ModelAdmin):
    inlines = [PlataformaStackedInLine]
    
admin.site.register(Bodega, BodegaAdmin)