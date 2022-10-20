from django.contrib import admin
from .models import ManualReading, ManualReadedBy


class ManualReadedByInline(admin.StackedInline):
    model = ManualReadedBy
    extra = 0


@admin.register(ManualReading)
class ManualReadingAdmin(admin.ModelAdmin):
    inlines = [ManualReadedByInline]
