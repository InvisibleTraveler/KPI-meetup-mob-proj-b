from django.contrib import admin
from .models import Meeting


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "start_at", "date_string", "is_main")
    list_filter = ("title", "created_at", "is_main")
    search_fields = ("title",)
