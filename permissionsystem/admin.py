from django.contrib import admin

from .models import (
    PermissionModule,
    RolePermission
)


# =====================================================
# Permission Module Admin
# =====================================================
@admin.register(PermissionModule)
class PermissionModuleAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'code',
    )


# =====================================================
# Role Permission Admin
# =====================================================
@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):

    list_display = (
        'role',
        'module',
        'can_view',
        'can_create',
        'can_update',
        'can_delete',
    )

    list_filter = (
        'role',
        'module',
    )