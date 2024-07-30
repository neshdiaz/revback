from django.contrib import admin

from equipos.models import Equipo


class EquipoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Equipo, EquipoAdmin)
