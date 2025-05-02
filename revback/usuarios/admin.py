from django.contrib import admin
from usuarios.models import Usuario
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin, GroupAdmin as DefaultGroupAdmin

# Desregistrar el modelo Group del admin predeterminado
admin.site.unregister(Group)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """Configuración personalizada para el modelo Usuario."""
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Registrar el modelo Group en la sección de autenticación y autorización
@admin.register(Group)
class GroupAdmin(DefaultGroupAdmin):
    """Configuración personalizada para el modelo Group."""
    list_display = ('name',)
    search_fields = ('name',)

# Registrar el modelo Permission (opcional)
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    """Configuración personalizada para el modelo Permission."""
    list_display = ('name', 'codename', 'content_type')
    search_fields = ('name', 'codename')

# Configuración del panel de administración
# Cambiar el título y el encabezado del sitio de administración
admin.site.site_header = "Panel Administrativo"
admin.site.index_title = "Bienvenido al Panel de Administración"

