from django.contrib import admin
from .models import OrganizationType, OurLadyBlessedTitle, Organization


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(OurLadyBlessedTitle)
class OurLadyBlessedTitleAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass
