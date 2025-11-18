from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.timezone import now
from .models import Rental
from notifications.models import Notification
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=Rental)
def rental_notifications(sender, instance, **kwargs):
    status = instance.status
    usr = instance.user
    admins = User.objects.filter(is_superuser=True)
    channel = get_channel_layer()

    # ============================
    # AWAITING VERIFICATION
    # ============================
    if status == "awaiting_verification":

        # Create admin notifications
        for admin in admins:
            Notification.objects.create(
                user=admin,
                message=f"Rental #{instance.id} menunggu verifikasi."
            )

        # Create user notification
        user_message = (
            f"Deposit dikirim. Rental #{instance.id} menunggu verifikasi admin."
        )

        Notification.objects.create(
            user=usr,
            message=user_message
        )

        # WebSocket push to user
        async_to_sync(channel.group_send)(
            f"notif_{usr.id}",
            {
                "type": "send_notification",
                "message": user_message,
                "timestamp": str(now()),
            }
        )

    # ============================
    # APPROVED
    # ============================
    if status == "approved":
        msg = f"Rental #{instance.id} disetujui."
        Notification.objects.create(user=usr, message=msg)

        async_to_sync(channel.group_send)(
            f"notif_{usr.id}",
            {
                "type": "send_notification",
                "message": msg,
                "timestamp": str(now()),
            }
        )

    # ============================
    # REJECTED
    # ============================
    if status == "rejected":
        msg = f"Rental #{instance.id} ditolak."
        Notification.objects.create(user=usr, message=msg)

        async_to_sync(channel.group_send)(
            f"notif_{usr.id}",
            {
                "type": "send_notification",
                "message": msg,
                "timestamp": str(now()),
            }
        )
