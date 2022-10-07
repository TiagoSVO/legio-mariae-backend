from django.contrib import admin
from .models import Member, MemberAddress
from addresses.forms import StackedAddressForm


class MemberAddressInline(StackedAddressForm):
    model = MemberAddress
    extra = 0


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['complete_name', 'cpf', 'nickname', 'birthday', 'email',
                           'deleted']}),
    ]

    inlines = [MemberAddressInline,]

    list_display = ['complete_name', 'nickname', 'birthday', 'deleted']
