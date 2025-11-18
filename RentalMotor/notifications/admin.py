from django.contrib import admin
from .models import Notification

# Register your models here.
# @admin.register(Notification)
# class AdminNotificationAdmin(admin.ModelAdmin):
#     list_display = ("user", "created_at", "is_read")
#     list_filter = ("is_read", "created_at")
#     ordering = ("-created_at",)
