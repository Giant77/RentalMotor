from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle

# Create your models here.
class AdminNotification(models.Model):
    rental = models.ForeignKey("rentals.Rental", on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notif #{self.id} • Rental {self.rental.id} • {self.created_at}"
