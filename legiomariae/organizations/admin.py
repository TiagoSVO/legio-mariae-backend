from django.contrib import admin
from .models import OrganizationType, OurLadyBlessedTitle, Organization, OrganizationAddress
from addresses.forms import StackedAddressForm


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(OurLadyBlessedTitle)
class OurLadyBlessedTitleAdmin(admin.ModelAdmin):
    pass


class OrganizationAddressInline(StackedAddressForm):
    model = OrganizationAddress
    extra = 0


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['registered_at', 'active', 'deleted', 'organization_type', 'our_blessed_lady_title', 'organization_parent']}),
    ]

    inlines = [OrganizationAddressInline]
