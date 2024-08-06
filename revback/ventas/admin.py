from django.contrib import admin
from ventas.models import Venta


class VentaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Venta, VentaAdmin)