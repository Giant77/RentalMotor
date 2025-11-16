from django.db import models
from django.conf import settings
from RentalMotor.views import unified_image_path

# Create your models here.
class Vehicle(models.Model):
    STATUS = (('available','Available'), ('rented','Rented'), ('pending','Pending'), ('maintenance','Maintenance'))
    plate = models.CharField(max_length=12, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True)
    year = models.PositiveSmallIntegerField(null=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS, default='available')
    image = models.ImageField(upload_to=unified_image_path, blank=True, null=True)
    notes = models.TextField(blank=True)
    tnc = models.TextField(blank=True)  # terms & conditions


    def __str__(self): return f"{self.plate} - {self.make} {self.model}"
