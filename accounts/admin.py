from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Custom user model import
from .models import User


# =====================================================
# Custom User Admin
# =====================================================
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # Admin panel এ list view তে যা দেখাবে
    list_display = (
        'username',
        'email',
        'role',
        'branch',
        'is_active',
    )

    # Filter sidebar
    list_filter = (
        'role',
        'branch',
        'is_active',
    )

    # Search option
    search_fields = (
        'username',
        'email',
    )