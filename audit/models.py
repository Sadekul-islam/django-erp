from django.db import models
from django.contrib.auth.models import User


# =====================================================
# 🧾 ADMIN AUDIT LOG (INFRASTRUCTURE LAYER)
# =====================================================
class AdminAuditLog(models.Model):

    # 👤 who did action
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    # 🧩 model name
    model_name = models.CharField(max_length=100)

    # 🆔 object id
    object_id = models.CharField(max_length=50, null=True, blank=True)

    # ⚙️ action type
    action = models.CharField(max_length=20)

    # 📦 old data
    old_data = models.TextField(null=True, blank=True)

    # 📦 new data
    new_data = models.TextField(null=True, blank=True)

    # 🏢 branch context
    branch = models.CharField(max_length=100, null=True, blank=True)

    # ⏰ timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.model_name}"