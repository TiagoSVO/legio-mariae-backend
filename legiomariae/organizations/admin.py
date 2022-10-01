from django.contrib import admin
from .models import OrganizationType, OurLadyBlessedTitle


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(OurLadyBlessedTitle)
class OurLadyBlessedTitleAdmin(admin.ModelAdmin):
    pass
