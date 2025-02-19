from django.contrib import admin
from plataformas.models import Plataforma, TipoPlataforma, CaracteristicasPlataforma

class CaracteristicasPlataformaInline(admin.TabularInline):
    model = CaracteristicasPlataforma
    extra = 0

class TipoPlataformaAdmin(admin.ModelAdmin):
    inlines = [CaracteristicasPlataformaInline]

class PlataformaAdmin(admin.ModelAdmin):
    inlines = [TipoPlataformaAdmin]

admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(TipoPlataforma, TipoPlataformaAdmin)