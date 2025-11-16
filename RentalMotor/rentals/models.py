from django.db import models
from django.conf import settings
from vehicles.models import Vehicle
from django.contrib.auth.models import User
from RentalMotor.views import unified_image_path

# Create your models here.
class Rental(models.Model):
    STATUS = (
        ("pending", "Pending"),
        ("awaiting_deposit", "Awaiting Deposit"),
        ("awaiting_verification", "Awaiting Verification"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    addons = models.JSONField(default=dict)  # processed via decorator pattern
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sim_image = models.ImageField(upload_to=unified_image_path, null=True, blank=True) # TODO: images
    status = models.CharField(max_length=30, choices=STATUS, default="pending")
    
    admin_reason = models.TextField(blank=True)
    reviewed_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="reviewed_rentals",
        on_delete=models.SET_NULL
    )

    created_at = models.DateTimeField(auto_now_add=True)

# class Transaction(models.Model):
#     booking = models.OneToOneField(Rental, on_delete=models.CASCADE)
#     total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     fines = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     finalized = models.BooleanField(default=False)
#     staff_confirmed = models.BooleanField(default=False)
#     user_confirmed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
