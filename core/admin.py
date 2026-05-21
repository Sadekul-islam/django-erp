from django.contrib import admin
from .models import Branch, AcademicSession


# Register Branch model
admin.site.register(Branch)


# Register Academic Session model
admin.site.register(AcademicSession)