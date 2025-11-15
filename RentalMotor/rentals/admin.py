from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rental

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "vehicle",
        "start_date",
        "end_date",
        "status",
        "deposit_amount",
        "reviewed_by",
        "admin_reason",
    )

    fields = (
        "user", 
        "vehicle",
        "start_date", 
        "end_date", 
        "addons",
        "deposit_amount", 
        "sim_image", # TODO: image implementations
        "status",
        "admin_reason", 
        "reviewed_by",
    )

    readonly_fields = ("reviewed_by",)

    actions = ["approve_rental", "reject_rental"]

    list_filter = ("status", "vehicle__make", "vehicle__model")

    search_fields = ("user__username", "vehicle__plate")

    actions = ["approve_rental", "reject_rental"]

    def approve_rental(self, request, queryset):
        for obj in queryset:
            obj.status = "approved"
            obj.reviewed_by = request.user
            obj.admin_reason = "Approved"
            obj.save()
        self.message_user(request, "Selected rentals have been approved.")

    approve_rental.short_description = "Approve selected rentals"

    def reject_rental(self, request, queryset):
        for obj in queryset:
            obj.status = "rejected"
            obj.reviewed_by = request.user
            if not obj.admin_reason:
                obj.admin_reason = "Rejected"
            obj.save()
        self.message_user(request, "Selected rentals have been rejected.")

    reject_rental.short_description = "Reject selected rentals"
