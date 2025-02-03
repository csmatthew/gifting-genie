from django.contrib import admin
from .models import Planner

# Register your models here.
@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'event_time', 'user')
    search_fields = ('event_name', 'user__username')
    list_filter = ('event_date', 'event_time', 'user')
    ordering = ('event_date', 'event_time')
    fieldsets = (
        (None, {
            'fields': ('event_name', 'event_date', 'event_time', 'user')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

