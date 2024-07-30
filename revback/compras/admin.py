from django.contrib import admin
from compras.models import Compra


class CompraAdmin(admin.ModelAdmin):
    pass


admin.site.register(Compra, CompraAdmin)
