from django.shortcuts import render, get_object_or_404
from .models import Vehicle

# Create your views here.
def home(request):
    vehicles = Vehicle.objects.all()
    return render(request, "home/home.html", {"vehicles": vehicles})


def vehicle_list(request):
    vtype = request.GET.get("type")
    queryset = Vehicle.objects.all()

    if vtype:
        queryset = queryset.filter(type__icontains=vtype)

    return render(request, "vehicles/vehicle_list.html", {"vehicles": queryset})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, "vehicles/vehicle_detail.html", {"vehicle": vehicle})
