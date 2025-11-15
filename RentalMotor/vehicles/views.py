from django.shortcuts import render
from django.shortcuts import render
from .models import Vehicle

# Create your views here.
def home(request):
    vehicles = Vehicle.objects.all()
    return render(request, "home.html", {"vehicles": vehicles})


def vehicle_list(request):
    vtype = request.GET.get("type")
    queryset = Vehicle.objects.all()

    if vtype:
        queryset = queryset.filter(type__icontains=vtype)

    return render(request, "vehicle_list.html", {"vehicles": queryset})

def vehicle_detail(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    return render(request, "vehicle_detail.html", {"vehicle": vehicle})
