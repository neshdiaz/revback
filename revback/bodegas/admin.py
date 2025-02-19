from django.contrib import admin, messages
from bodegas.models import Bodega
from plataformas.models import Plataforma
class PlataformaStackedInLine(admin.TabularInline):
    model = Plataforma
    extra = 0

class BodegaAdmin(admin.ModelAdmin):
    inlines = [PlataformaStackedInLine]
    def has_add_permission(self, request):
        # Si el usuario intenta agregar un nuevo registro, muestra un mensaje
        if request.method == 'POST':
            messages.warning(request, "No es posible agregar plataformas desde esta vista. Debe realizarlo a través de la opción de traslados, o realizando una nueva compra.")
        return False

admin.site.register(Bodega, BodegaAdmin)
