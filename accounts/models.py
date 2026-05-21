from django.db import models
from django.contrib.auth.models import AbstractUser

# Branch model import
from core.models import Branch


# =====================================================
# Custom User Model
# =====================================================
class User(AbstractUser):

    # =========================================
    # User Role Choices
    # =========================================
    ROLE_CHOICES = (

        ('super_admin', 'Super Admin'),
        ('branch_admin', 'Branch Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('guardian', 'Guardian'),
        ('accountant', 'Accountant'),
        ('staff', 'Staff'),
    )

    # =========================================
    # User Role
    # =========================================
    role = models.CharField(

        max_length=30,

        choices=ROLE_CHOICES,

        # Default role
        default='student'
    )

    # =========================================
    # User Branch
    # =========================================
    branch = models.ForeignKey(

        Branch,

        # Branch delete হলেও user থাকবে
        on_delete=models.SET_NULL,

        # Database NULL allowed
        null=True,

        # Admin form required
        blank=False
    )

    # =========================================
    # Profile Image
    # =========================================
    profile_image = models.ImageField(

        upload_to='profiles/',

        blank=True,
        null=True
    )

    # =========================================
    # Active Status
    # =========================================
    is_active = models.BooleanField(
        default=True
    )

    # =========================================
    # Created Time
    # =========================================
    created_at = models.DateTimeField(
    auto_now_add=True,
    null=True
)

    def __str__(self):

        return self.username
    
        # =====================================================
    # Role Checking Helper Methods
    # -----------------------------------------------------
    # এগুলো future permission system এ use হবে
    # =====================================================

    # Super Admin check
    def is_super_admin(self):

        return self.role == 'super_admin'

    # Branch Admin check
    def is_branch_admin(self):

        return self.role == 'branch_admin'

    # Teacher check
    def is_teacher(self):

        return self.role == 'teacher'

    # Student check
    def is_student(self):

        return self.role == 'student'

    # Guardian check
    def is_guardian(self):

        return self.role == 'guardian'

    # Accountant check
    def is_accountant(self):

        return self.role == 'accountant'