from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedStackedInline

from .models import Work, ParticipationType, WorkReportStatus, \
                    WorkSheet, WorkSheetItem, WorkSheetItemMemberFiliation, \
                    WorkReport


class WorkReportInline(NestedStackedInline):
    model = WorkReport
    extra = 1
    max_num = 1


class WorkSheetItemMemberFiliationInline(NestedStackedInline):
    model = WorkSheetItemMemberFiliation
    extra = 1


class WorkSheetItemInline(NestedStackedInline):
    model = WorkSheetItem
    extra = 1

    inlines = [WorkSheetItemMemberFiliationInline, WorkReportInline]


@admin.register(WorkSheet)
class WorkSheetAdmin(NestedModelAdmin):
    inlines = [WorkSheetItemInline]


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(ParticipationType)
class ParticipationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkReportStatus)
class WorkReportStatusAdmin(admin.ModelAdmin):
    pass
