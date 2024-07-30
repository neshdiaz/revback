from django.contrib import admin

from plataformas.models import Plataforma
from plataformas.models import TipoPlataforma


class PlataformaAdmin(admin.ModelAdmin):
    pass


class TipoPlataformaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(TipoPlataforma, TipoPlataformaAdmin)
