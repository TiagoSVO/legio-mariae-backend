from django.contrib import admin
from .models import Member, MemberAddress, MemberPhone, MemberFiliationType, \
                    MemberFiliation, PostOffice, PostOfficeMemberFiliation
from addresses.forms import StackedAddressForm
from nested_admin import NestedModelAdmin, NestedStackedInline


class MemberPhoneInline(NestedStackedInline):
    model = MemberPhone
    extra = 0


class MemberAddressInline(StackedAddressForm, NestedStackedInline):
    model = MemberAddress
    extra = 0


class PostOfficeMemberFiliationInline(NestedStackedInline):
    model = PostOfficeMemberFiliation
    extra = 0
    max_num = 1


class MemberFiliationInline(NestedStackedInline):
    model = MemberFiliation
    extra = 0

    inlines = [PostOfficeMemberFiliationInline,]



@admin.register(Member)
class MemberAdmin(NestedModelAdmin):
    fieldsets = [
        (None, {'fields': ['complete_name', 'cpf', 'nickname', 'birthday', 'email',
                           'deleted']}),
    ]

    inlines = [MemberAddressInline, MemberPhoneInline, MemberFiliationInline]

    list_display = ['complete_name', 'nickname', 'birthday', 'deleted']


@admin.register(MemberFiliationType)
class MemberFiliationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(PostOffice)
class PostOfficeAdmin(admin.ModelAdmin):
    pass

