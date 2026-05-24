# =====================================================
# Django Template Import
# =====================================================

from django import template


# =====================================================
# Permission Function Import
# =====================================================

from core.permissions import can_user_access_module


# =====================================================
# Template Register
# =====================================================

register = template.Library()


# =====================================================
# Template Permission Tag
# =====================================================

@register.simple_tag

def has_module_permission(

    user,
    module_code,
    action='view'

):

    return can_user_access_module(

        user,
        module_code,
        action

    )