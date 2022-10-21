from django.contrib import admin
from .models import AttendenceSheet, AttendenceSheetMember, AttendenceSheetMemberStatus


class AttendenceSheetMemberAdmin(admin.StackedInline):
    model = AttendenceSheetMember


@admin.register(AttendenceSheet)
class AttendenceSheetAdmin(admin.ModelAdmin):
    inlines = [AttendenceSheetMemberAdmin]


@admin.register(AttendenceSheetMemberStatus)
class AttendenceSheetMemberStatusAdmin(admin.ModelAdmin):
    pass
