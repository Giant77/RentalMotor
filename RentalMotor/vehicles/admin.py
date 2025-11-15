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
        (  #TODO: update for images!
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