from django.db import models

# Base model import
from core.models import BaseModel


# =====================================================
# Permission Module
# -----------------------------------------------------
# ERP এর feature/module permissions manage করবে
# =====================================================
class PermissionModule(BaseModel):

    # Module name
    name = models.CharField(
        max_length=100,
        unique=True
    )

    # Module code
    code = models.CharField(
        max_length=100,
        unique=True
    )

    # Module description
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name


# =====================================================
# Role Permission System
# -----------------------------------------------------
# কোন role কোন module access পাবে
# =====================================================
class RolePermission(BaseModel):

    ROLE_CHOICES = (

        ('super_admin', 'Super Admin'),
        ('branch_admin', 'Branch Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('guardian', 'Guardian'),
        ('accountant', 'Accountant'),
        ('staff', 'Staff'),
    )

    # কোন role
    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES
    )

    # কোন module
    module = models.ForeignKey(

        PermissionModule,

        on_delete=models.CASCADE,

        related_name='permissions'
    )

    # View permission
    can_view = models.BooleanField(
        default=False
    )

    # Create permission
    can_create = models.BooleanField(
        default=False
    )

    # Update permission
    can_update = models.BooleanField(
        default=False
    )

    # Delete permission
    can_delete = models.BooleanField(
        default=False
    )

    def __str__(self):

        return f"{self.role} -> {self.module.name}"