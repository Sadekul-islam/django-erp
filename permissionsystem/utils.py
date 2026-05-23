# =====================================================
# Role Permission Import
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
    # Super Admin সব access পাবে
    # =================================================

    if user.is_superuser:

        return True



    # =================================================
    # User role collect
    # =================================================

    role = user.role



    # =================================================
    # Role permission find
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
    # View Permission
    # =================================================

    if action == 'view':

        return permission.can_view



    # =================================================
    # Create Permission
    # =================================================

    elif action == 'create':

        return permission.can_create



    # =================================================
    # Update Permission
    # =================================================

    elif action == 'update':

        return permission.can_update



    # =================================================
    # Delete Permission
    # =================================================

    elif action == 'delete':

        return permission.can_delete



    # =================================================
    # Unknown action হলে deny
    # =================================================

    return False