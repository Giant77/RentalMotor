from django.db import models
from django.conf import settings
from RentalMotor.vehicles.models import Vehicle

# Create your models here.
class Booking(models.Model):
    PENDING, ACCEPTED, REJECTED, RETURNED = 'pending','accepted','rejected','returned'
    STATUS_CHOICES = [(PENDING,'Pending'), (ACCEPTED,'Accepted'), (REJECTED,'Rejected'), (RETURNED,'Returned')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    guarantee_doc = models.CharField(max_length=255, blank=True)  # e.g., path to scanned SIM/KTP
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fines = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    finalized = models.BooleanField(default=False)
    staff_confirmed = models.BooleanField(default=False)
    user_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
