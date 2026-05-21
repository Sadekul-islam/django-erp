# =====================================================
# Role Permission Checker Utilities
# =====================================================

from .models import RolePermission


# =====================================================
# Check user permission
# -----------------------------------------------------
# Example:
#
# can_user_access_module(
#     request.user,
#     'finance',
#     'view'
# )
# =====================================================
def can_user_access_module(

    user,
    module_code,
    action
):

    # =================================================
    # Super admin can access everything
    # =================================================
    if user.role == 'super_admin':

        return True

    try:

        # =================================================
        # Role permission lookup
        # =================================================
        permission = RolePermission.objects.get(

            role=user.role,

            module__code=module_code
        )

        # =================================================
        # Action checking
        # =================================================
        if action == 'view':

            return permission.can_view

        elif action == 'create':

            return permission.can_create

        elif action == 'update':

            return permission.can_update

        elif action == 'delete':

            return permission.can_delete

        # Invalid action
        return False

    except RolePermission.DoesNotExist:

        # Permission না থাকলে deny
        return False