from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required
def mark_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return JsonResponse({"status": "ok"})

@login_required
def delete_notif(request, notif_id):
    Notification.objects.filter(id=notif_id, user=request.user).delete()
    return JsonResponse({"status": "ok"})

@login_required
def list_notifications(request):
    qs = Notification.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "notifications/list.html", {"data": qs})

@staff_member_required
def admin_list(request):
    data = Notification.objects.all().order_by("-created_at")
    return render(request, "notifications/admin_list.html", {"data": data})

