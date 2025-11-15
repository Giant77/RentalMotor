from django.urls import path
from . import views

app_name = "rental"

urlpatterns = [
    path("start/<int:vehicle_id>/", views.start_rental, name="start_rental"),
    path("deposit/<int:rental_id>/", views.deposit, name="deposit"),
    path("pending/<int:rental_id>/", views.pending, name="pending"),]
