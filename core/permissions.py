# =====================================================
# Model Import
# =====================================================

from .models import RolePermission


# =====================================================
# Check User Module Permission
# -----------------------------------------------------
# User কোন module access পাবে কিনা check করবে
# =====================================================

def can_user_access_module(

    user,
    module_code,
    action='view'

):

    # =================================================
    # User login কিনা check
    # =================================================

    if not user.is_authenticated:

        return False

    # =================================================
    # Super Admin সব access পাবে
    # =================================================

    if user.is_superuser:

        return True

    # =================================================
    # User Role collect
    # =================================================

    role = getattr(
        user,
        'role',
        None
    )

    # =================================================
    # Role না থাকলে deny
    # =================================================

    if not role:

        return False

    # =================================================
    # Permission find
    # =================================================

    permission = RolePermission.objects.filter(

        role=role,

        module__code=module_code

    ).first()

    # =================================================
    # Permission না থাকলে deny
    # =================================================

    if not permission:

        return False

    # =================================================
    # Permission Map
    # =================================================

    permission_map = {

        'view': permission.can_view,

        'create': permission.can_create,

        'update': permission.can_update,

        'delete': permission.can_delete,

    }

    # =================================================
    # Final Return
    # =================================================

    return permission_map.get(
        action,
        False
    )