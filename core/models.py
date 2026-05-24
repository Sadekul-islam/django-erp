# =====================================================
# Django Import
# =====================================================

from django.db import models


# =====================================================
# Base Model
# -----------------------------------------------------
# Common reusable fields
# =====================================================

class BaseModel(models.Model):

    # =================================================
    # Created Time
    # =================================================

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    # =================================================
    # Updated Time
    # =================================================

    updated_at = models.DateTimeField(

        auto_now=True

    )

    # =================================================
    # Active Status
    # =================================================

    is_active = models.BooleanField(

        default=True

    )

    # =================================================
    # Abstract Model
    # =================================================

    class Meta:

        abstract = True


# =====================================================
# Branch Model
# -----------------------------------------------------
# Company Branch / Office
# =====================================================

class Branch(BaseModel):

    # =================================================
    # Branch Name
    # =================================================

    name = models.CharField(

        max_length=200

    )

    # =================================================
    # Branch Code
    # =================================================

    code = models.CharField(

        max_length=50,

        unique=True

    )

    # =================================================
    # Branch Address
    # =================================================

    address = models.TextField(

        blank=True,

        null=True

    )

    # =================================================
    # Admin Display
    # =================================================

    def __str__(self):

        return self.name


# =====================================================
# Role Model
# =====================================================

class Role(BaseModel):

    name = models.CharField(

        max_length=100,

        unique=True

    )

    def __str__(self):

        return self.name


# =====================================================
# Module Model
# =====================================================

class Module(BaseModel):

    name = models.CharField(

        max_length=100

    )

    code = models.CharField(

        max_length=100,

        unique=True

    )

    def __str__(self):

        return self.name

# =====================================================
# Role Permission Model
# =====================================================

class RolePermission(BaseModel):

    role = models.ForeignKey(

        Role,

        on_delete=models.CASCADE

    )

    module = models.ForeignKey(

        Module,

        on_delete=models.CASCADE

    )

    can_view = models.BooleanField(

        default=False

    )

    can_create = models.BooleanField(

        default=False

    )

    can_update = models.BooleanField(

        default=False

    )

    can_delete = models.BooleanField(

        default=False

    )

    class Meta:

        unique_together = (

            'role',

            'module'

        )

    def __str__(self):

        return f"{self.role} - {self.module}"