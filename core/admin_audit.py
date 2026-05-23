from audit.models import AdminAuditLog


# =====================================================
# 🧠 ADMIN AUDIT MIXIN
# =====================================================
# এই mixin Django admin এ attach করলে:
# 👉 automatic logging start হবে
# =====================================================
class AdminAuditMixin:

    # =================================================
    # 💾 SAVE MODEL (CREATE + UPDATE TRACKING)
    # =================================================
    def save_model(self, request, obj, form, change):

        # 👤 current logged-in user
        user = request.user

        # =================================================
        # 📦 old_data store করার জন্য variable
        # =================================================
        old_data = None

        # =================================================
        # ⚠️ যদি এটা update হয় (new create না)
        # =================================================
        if change:

            # আগের data database থেকে নিয়ে আসা
            old_instance = self.model.objects.get(pk=obj.pk)

            # old object কে string এ convert করা
            old_data = str(old_instance.__dict__)

        # =================================================
        # 💾 আসল object save করা হচ্ছে database এ
        # =================================================
        super().save_model(request, obj, form, change)

        # =================================================
        # 📦 নতুন data capture করা হচ্ছে
        # =================================================
        new_data = str(obj.__dict__)

        # =================================================
        # 🧾 AUDIT LOG SAVE করা হচ্ছে
        # =================================================
        AdminAuditLog.objects.create(
            user=user,  # কে করেছে
            model_name=self.model.__name__,  # কোন model
            object_id=obj.pk,  # কোন record
            action="UPDATE" if change else "CREATE",  # কি action
            old_data=old_data,  # পুরানো data
            new_data=new_data,  # নতুন data
            branch=getattr(user, "branch", None)  # branch info
        )

    # =================================================
    # 🗑 DELETE MODEL TRACKING
    # =================================================
    def delete_model(self, request, obj):

        # 📦 delete করার আগে data save করা
        old_data = str(obj.__dict__)

        # 🧨 আসল delete operation
        super().delete_model(request, obj)

        # 🧾 delete log save করা হচ্ছে
        AdminAuditLog.objects.create(
            user=request.user,  # কে delete করেছে
            model_name=self.model.__name__,  # কোন model
            object_id=obj.pk,  # কোন record
            action="DELETE",  # action type
            old_data=old_data,  # delete হওয়া data
            new_data=None,  # delete এর পরে কিছু নেই
            branch=getattr(request.user, "branch", None)  # branch
        )