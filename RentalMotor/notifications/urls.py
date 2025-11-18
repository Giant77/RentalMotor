from django.urls import path
from . import views

urlpatterns = [
    path("mark-read/", views.mark_read, name="mark_read"),
    path("delete/<int:notif_id>/", views.delete_notif, name="delete_notif"),
    path("", views.list_notifications, name="list"),
]