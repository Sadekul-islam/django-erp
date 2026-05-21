
from django.contrib import admin

from .models import Product


# =====================================================
# Product Admin
# =====================================================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # List page columns
    list_display = (
        'name',
        'price',
        'branch',
    )

    # Right-side filters
    list_filter = (
        'branch',
    )