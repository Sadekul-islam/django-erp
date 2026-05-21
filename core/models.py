from django.db import models

# Django এর current logged-in user model import
from django.conf import settings

# =========================================
# Base model for all future models
# =========================================
class BaseModel(models.Model):

    # =====================================================
    # Record created time
    # =====================================================
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # =====================================================
    # Record updated time
    # =====================================================
    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =====================================================
    # Record active status
    # =====================================================
    is_active = models.BooleanField(
        default=True
    )

    # =====================================================
    # Soft delete support
    # True = deleted logically
    # False = visible normally
    # =====================================================
    is_deleted = models.BooleanField(
        default=False
    )

    # =====================================================
    # কে record create করেছে
    # =====================================================
    created_by = models.ForeignKey(

        # Current custom user model
        settings.AUTH_USER_MODEL,

        # Empty রাখা যাবে
        null=True,
        blank=True,

        # User delete হলে NULL হবে
        on_delete=models.SET_NULL,

        # Reverse relation name
        related_name="created_%(class)s_set"
    )

    # =====================================================
    # কে record update করেছে
    # =====================================================
    updated_by = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        null=True,
        blank=True,

        on_delete=models.SET_NULL,

        related_name="updated_%(class)s_set"
    )

    # =====================================================
    # Soft delete method
    # =====================================================
    def soft_delete(self):

        self.is_deleted = True
        self.save()

    class Meta:

        # Direct table create হবে না
        abstract = True

# =========================================
# Multi Branch System
# =========================================
class Branch(BaseModel):

    # Branch name
    name = models.CharField(max_length=255)

    # Unique branch code
    code = models.CharField(max_length=50, unique=True)

    # Branch address
    address = models.TextField()

    # Contact number
    phone = models.CharField(max_length=20)

    # Branch email
    email = models.EmailField(blank=True, null=True)

    def __str__(self):

        return self.name


# =========================================
# Academic Session System
# =========================================
class AcademicSession(BaseModel):

    # Academic year
    year = models.CharField(max_length=20)

    # Session start date
    start_date = models.DateField()

    # Session end date
    end_date = models.DateField()

    # Current active session
    is_current = models.BooleanField(default=False)

    # =========================================
    # Admin panel এ session name দেখাবে
    # =========================================
    def __str__(self):

        return self.year