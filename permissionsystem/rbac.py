"""
RBAC PERMISSION SYSTEM v2

এই system এর কাজ:

✔ Role based access control
✔ Module + Action permission mapping
✔ Central permission engine
✔ Future SaaS scalable design
"""

# =====================================================
# 🔐 MAIN PERMISSION CHECK FUNCTION
# =====================================================
def can_user_access_module(user, module, action):

    # =================================================
    # 🔥 SUPER ADMIN BYPASS
    # =================================================
    if user.is_superuser:
        return True

    # =================================================
    # ❌ NO ROLE = NO ACCESS
    # =================================================
    if not hasattr(user, "role"):
        return False

    role = user.role

    # =================================================
    # 🔐 SIMPLE ROLE MATRIX (can move to DB later)
    # =================================================
    PERMISSIONS = {

        # Inventory module rules
        "inventory": {
            "admin": ["view", "add", "edit", "delete"],
            "manager": ["view", "add", "edit"],
            "staff": ["view"]
        },

        # HR module rules
        "hr": {
            "admin": ["view", "add", "edit", "delete"],
            "staff": ["view"]
        }
    }

    # =================================================
    # 🔍 CHECK MODULE EXISTS
    # =================================================
    if module not in PERMISSIONS:
        return False

    # =================================================
    # 🔍 CHECK ROLE EXISTS
    # =================================================
    if role not in PERMISSIONS[module]:
        return False

    # =================================================
    # 🔍 FINAL ACTION CHECK
    # =================================================
    return action in PERMISSIONS[module][role]