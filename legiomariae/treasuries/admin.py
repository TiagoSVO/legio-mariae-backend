from django.contrib import admin

from .models import TreasuryReport, Expense


class ExpenseInline(admin.StackedInline):
    model = Expense
    extra = 0


@admin.register(TreasuryReport)
class TreasuryReportAdmin(admin.ModelAdmin):
    inlines = [ExpenseInline]
