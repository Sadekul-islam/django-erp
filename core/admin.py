# =====================================================
# Django Admin Import
# =====================================================

from django.contrib import admin


# =====================================================
# Model Import
# =====================================================

from .models import (
    BaseModel,
    Branch,
    Role,
    Module,
    RolePermission
)


# =====================================================
# Register Models
# =====================================================

admin.site.register(Role)

admin.site.register(Module)

admin.site.register(RolePermission)