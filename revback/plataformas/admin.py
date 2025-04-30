from django.contrib import admin
from .models import Plataforma, TipoPlataforma, CaracteristicasPlataforma

# Inline para CaracteristicasPlataforma
class CaracteristicasPlataformaInline(admin.StackedInline):
    model = CaracteristicasPlataforma
    extra = 0

# Inline para Plataforma
class PlataformaInline(admin.StackedInline):
    model = Plataforma
    extra = 0

# Modelo Admin para TipoPlataforma
class TipoPlataformaAdmin(admin.ModelAdmin):
    inlines = [CaracteristicasPlataformaInline, PlataformaInline]
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

# Registrar los modelos en el admin
admin.site.register(TipoPlataforma, TipoPlataformaAdmin)
admin.site.register(Plataforma)
#admin.site.register(CaracteristicasPlataforma)
