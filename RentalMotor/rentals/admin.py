from django.contrib import admin
from .models import Rental

# Register your models here.
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

    list_filter = ("status", "vehicle__make", "vehicle__model")

    search_fields = ("user__username", "vehicle__plate")

    actions = ["approve_rental", "reject_rental", "complete_rental"]

    #
    # APPROVE via STATE PATTERN
    #
    def approve_rental(self, request, queryset):
        for obj in queryset:
            obj.reviewed_by = request.user
            obj.admin_reason = obj.admin_reason or "Approved"
            obj.approve()         # State pattern call
        self.message_user(request, "Selected rentals approved.")
    approve_rental.short_description = "Approve selected rentals"

    #
    # REJECT via STATE PATTERN
    #
    def reject_rental(self, request, queryset):
        for obj in queryset:
            obj.reviewed_by = request.user
            obj.admin_reason = obj.admin_reason or "Rejected"
            obj.reject()          
    
        self.message_user(request, "Selected rentals rejected.")
    reject_rental.short_description = "Reject selected rentals"

    #
    # FINALIZE / COMPLETE (return vehicle)
    #
    def complete_rental(self, request, queryset):
        for obj in queryset:
            obj.reviewed_by = request.user
            obj.admin_reason = obj.admin_reason or "Completed"
            obj.complete()        
    
        self.message_user(request, "Selected rentals marked as completed.")
    complete_rental.short_description = "Mark rentals as completed"
