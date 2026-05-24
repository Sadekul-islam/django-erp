# =====================================================
# Django Imports
# =====================================================

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# =====================================================
# Local Imports
# =====================================================

from .models import Product

from permissionsystem.utils import can_user_access_module


# =====================================================
# Product List View
# =====================================================

@login_required
def product_list(request):

    # =================================================
    # Permission check
    # =================================================

    allowed = can_user_access_module(

        request.user,
        'inventory',
        'view'
    )



    # =================================================
    # DEBUG
    # =================================================

    print("USER ROLE:", request.user.role)

    print("ALLOWED:", allowed)



    # =================================================
    # Permission deny
    # =================================================

    if not allowed:

        return HttpResponseForbidden(

            "Permission Denied"

        )



    # =================================================
    # Product queryset
    # =================================================

    products = Product.objects.all()



    # =================================================
    # Render template
    # =================================================

    return render(

        request,

        'inventory/product_list.html',

        {
            'products': products
        }

    )