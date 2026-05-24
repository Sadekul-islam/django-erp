# =====================================================
# Http Response Import
# =====================================================

from django.http import HttpResponseForbidden


# =====================================================
# Permission Function Import
# =====================================================

from .permissions import can_user_access_module


# =====================================================
# Module Permission Decorator
# =====================================================

def module_permission_required(

    module_code,
    action='view'

):

    # =================================================
    # Decorator Function
    # =================================================

    def decorator(view_func):

        # =============================================
        # Wrapper Function
        # =============================================

        def wrapper(request, *args, **kwargs):

            # =========================================
            # Permission Check
            # =========================================

            if not can_user_access_module(

                request.user,

                module_code,

                action

            ):

                return HttpResponseForbidden(

                    "Permission Denied"

                )

            # =========================================
            # Original View Run
            # =========================================

            return view_func(

                request,

                *args,

                **kwargs

            )

        return wrapper

    return decorator