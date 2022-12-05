from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedStackedInline

from .models import Meeting, MeetingOrganizationJoin, WelcomeGuest, MeetingMinute, MeetingMinuteReaded
from .forms import WelcomeGuestForm

from treasuries.models import TreasuryReport, Expense
from manuals.models import ManualReading, ManualReadedBy
from attendences.models import AttendenceSheet, AttendenceSheetMember
from works.models import WorkSheet, WorkSheetItem, WorkSheetItemMemberFiliation, WorkReport


class MeetingOrganizationJoinInline(NestedStackedInline):
    model = MeetingOrganizationJoin
    extra = 0


class WelcomeGuestInline(NestedStackedInline):
    model = WelcomeGuest
    extra = 0
    form = WelcomeGuestForm


class MeetingMinuteInline(NestedStackedInline):
    model = MeetingMinute
    extra = 0
    min_num = 0
    max_num = 1


class MeetingMinuteReadedInline(NestedStackedInline):
    model = MeetingMinuteReaded
    extra = 0
    min_num = 1


class ExpenseInline(NestedStackedInline):
    model = Expense
    extra = 0
    min_num = 1


class TreasuryReportInline(NestedStackedInline):
    model = TreasuryReport
    extra = 0
    min_num = 1
    inlines = [ExpenseInline]


class ManualReadedByInline(NestedStackedInline):
    model = ManualReadedBy
    extra = 0
    min_num = 1


class ManualReadingInline(NestedStackedInline):
    model = ManualReading
    extra = 0
    min_num = 1
    max_num = 1

    inlines = [ManualReadedByInline]


class AttendenceSheetMemberInline(NestedStackedInline):
    model = AttendenceSheetMember
    extra = 0
    min_num = 1


class AttendenceSheetInline(NestedStackedInline):
    model = AttendenceSheet

    inlines = [AttendenceSheetMemberInline]


class WorkSheetItemMemberFiliationInline(NestedStackedInline):
    model = WorkSheetItemMemberFiliation
    extra = 0
    min_num = 2


class WorkSheetItemInline(NestedStackedInline):
    model = WorkSheetItem
    extra = 0
    min_num = 1

    inlines = [WorkSheetItemMemberFiliationInline]


class WorkSheetInline(NestedStackedInline):
    model = WorkSheet
    extra = 0
    min_num = 1

    inlines = [WorkSheetItemInline]


class WorkReportInline(NestedStackedInline):
    model = WorkReport
    extra = 0
    min_num = 1


@admin.register(Meeting)
class MeetingAdmin(NestedModelAdmin):
    inlines = [MeetingOrganizationJoinInline, WelcomeGuestInline,
               MeetingMinuteInline, MeetingMinuteReadedInline,
               TreasuryReportInline, ManualReadingInline,
               AttendenceSheetInline, WorkSheetInline,
               WorkReportInline]


@admin.register(MeetingMinute)
class MeetingMinuteAdmin(admin.ModelAdmin):
    change_form_template = 'meetings/meeting_minute/custom_change_form.html'
