from django.contrib import admin
from bodegas.models import Bodega


class BodegaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bodega, BodegaAdmin)
