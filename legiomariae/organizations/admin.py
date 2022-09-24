from django.contrib import admin
from .models import OrganizationType


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    pass
