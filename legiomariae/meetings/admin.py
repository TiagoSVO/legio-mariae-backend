from django.contrib import admin
from .models import Meeting, MeetingOrganizationJoin, WelcomeGuest, MinuteMeeting, MinuteMeetingReaded
from .forms import WelcomeGuestForm
from nested_admin import NestedModelAdmin, NestedStackedInline
from treasuries.models import TreasuryReport, Expense
from manuals.models import ManualReading, ManualReadedBy


class MeetingOrganizationJoinInline(NestedStackedInline):
    model = MeetingOrganizationJoin
    extra = 0


class WelcomeGuestInline(NestedStackedInline):
    model = WelcomeGuest
    extra = 0
    form = WelcomeGuestForm


class MinuteMeetingInline(NestedStackedInline):
    model = MinuteMeeting
    extra = 1
    max_num = 1


class MinuteMeetingReadedInline(NestedStackedInline):
    model = MinuteMeetingReaded
    extra = 1


class ExpenseInline(NestedStackedInline):
    model = Expense
    extra = 1


class TreasuryReportInline(NestedStackedInline):
    model = TreasuryReport
    extra = 1
    max_num = 1

    inlines = [ExpenseInline]


class ManualReadedByInline(NestedStackedInline):
    model = ManualReadedBy
    extra = 1


class ManualReadingInline(NestedStackedInline):
    model = ManualReading
    extra = 1
    max_num = 1

    inlines = [ManualReadedByInline]


@admin.register(Meeting)
class MeetingAdmin(NestedModelAdmin):
    inlines = [MeetingOrganizationJoinInline, WelcomeGuestInline,
               MinuteMeetingInline, MinuteMeetingReadedInline,
               TreasuryReportInline, ManualReadingInline]


@admin.register(MinuteMeeting)
class MinuteMeetingAdmin(admin.ModelAdmin):
    pass