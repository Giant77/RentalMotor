from django.contrib import admin
from .models import AdminNotification

# Register your models here.

@admin.register(AdminNotification)
class AdminNotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "rental", "vehicle", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    ordering = ("-created_at",)
