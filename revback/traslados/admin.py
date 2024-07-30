from django.contrib import admin

from traslados.models import Traslado


class TrasladoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Traslado, TrasladoAdmin)
