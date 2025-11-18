from .models import Notification

def user_notifications(request):
    if not request.user.is_authenticated:
        return {"notif_unread": 0, "notifications": []}

    qs = Notification.objects.filter(user=request.user).order_by("-created_at")
    return {
        "notif_unread": qs.filter(is_read=False).count(),
        "notifications": qs[:5],
    }
