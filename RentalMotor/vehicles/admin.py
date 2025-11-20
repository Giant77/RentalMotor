from django.contrib import admin
from .models import Vehicle

# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "plate",
        "make",
        "model",
        "year",
        "price_per_day",
        "status",
    )

    list_filter = ("status", "make", "year")

    search_fields = ("plate", "make", "model")

    ordering = ("plate",)

    fieldsets = [
        (
            "Informasi Utama",
            {
                "fields": (
                    "plate",
                    "make",
                    "model",
                    "year",
                    "price_per_day",
                    "status",
                )
            },
        ),
        (
            "Media",
            {
                "fields": ("image",),
            },
        ),
        (
            "Detail Tambahan",
            {
                "fields": ("notes", "tnc"),
            },
        ),
    ]
    
    actions = ["set_available", "set_maintenance"]

    #
    # set available via STATE PATTERN
    #
    def set_available(self, request, queryset):
        for obj in queryset:
            obj.available()

    set_available.short_description = "Set selected vehicles available"

    #
    # set maintenance via STATE PATTERN
    #
    def set_maintenance(self, request, queryset):
        for obj in queryset:
            obj.maintenance()          

    set_maintenance.short_description = "Set selected vehicles maintenance"
