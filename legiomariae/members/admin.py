from django.contrib import admin
from .models import Member, MemberAddress, MemberPhone
from addresses.forms import StackedAddressForm


class MemberPhoneInline(admin.StackedInline):
    model = MemberPhone
    extra = 0


class MemberAddressInline(StackedAddressForm):
    model = MemberAddress
    extra = 0


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['complete_name', 'cpf', 'nickname', 'birthday', 'email',
                           'deleted']}),
    ]

    inlines = [MemberAddressInline, MemberPhoneInline]

    list_display = ['complete_name', 'nickname', 'birthday', 'deleted']
