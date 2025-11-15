from django.urls import path
from . import views

# TODO: placeholder only! replace real views
urlpatterns = [
    path("", views.home, name="home"),
    path("vehicles/", views.vehicle_list, name="vehicle_list"),
    path("vehicle/<int:pk>/", views.vehicle_detail, name="vehicle_detail"),]
