from django.contrib import admin

from usuarios.models import Usuario, Permiso


class UsuarioAdmin(admin.ModelAdmin):
    pass


class PermisoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Permiso, PermisoAdmin)
