from django.contrib import admin
from .models import Meeting, MeetingOrganizationJoin, WelcomeGuest, MinuteMeeting, MinuteMeetingReaded
from .forms import WelcomeGuestForm
from nested_admin import NestedModelAdmin, NestedStackedInline


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


@admin.register(Meeting)
class MeetingAdmin(NestedModelAdmin):
    inlines = [MeetingOrganizationJoinInline, WelcomeGuestInline,
               MinuteMeetingInline, MinuteMeetingReadedInline]


@admin.register(MinuteMeeting)
class MinuteMeetingAdmin(admin.ModelAdmin):
    pass