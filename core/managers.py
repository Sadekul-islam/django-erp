from django.db import models


# =====================================================
# 🧠 SOFT DELETE MANAGER (CORE ENGINE)
# =====================================================
class SoftDeleteManager(models.Manager):

    # =================================================
    # 🔍 ACTIVE OBJECTS ONLY
    # =================================================
    def get_queryset(self):

        # parent queryset নেওয়া হচ্ছে
        qs = super().get_queryset()

        # ❌ is_deleted=True সব hide করে দিচ্ছি
        return qs.filter(is_deleted=False)