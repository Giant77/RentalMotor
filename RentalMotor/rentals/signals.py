from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Rental
from notifications.models import AdminNotification


@receiver(post_save, sender=Rental)
def create_admin_notification(sender, instance, created, **kwargs):
    if instance.status == "awaiting_verification":
        AdminNotification.objects.create(
            rental=instance,
            vehicle=instance.vehicle,
            message=(
                f"Rental ID {instance.id} dari {instance.user.username} "
                f"menunggu verifikasi untuk kendaraan {instance.vehicle.make} {instance.vehicle.model}"
            )
        )
