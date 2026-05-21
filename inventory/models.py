from django.db import models

# BaseModel import
from core.models import BaseModel

# Branch model import
from core.models import Branch


# =====================================================
# Product Model
# =====================================================
class Product(BaseModel):

    # Product name
    name = models.CharField(
        max_length=255
    )

    # Product price
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # =================================================
    # Branch Isolation Field
    # -------------------------------------------------
    # কোন branch এর product
    # =================================================
    # =================================================
# Branch Isolation Field
# -------------------------------------------------
# Temporarily NULL allowed for safe migration
# =================================================
    branch = models.ForeignKey(

    Branch,

    on_delete=models.CASCADE,

    related_name='products',

    # Existing old data এর জন্য
    null=True,
    blank=True
)

    def __str__(self):

        return self.name