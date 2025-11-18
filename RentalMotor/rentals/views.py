from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.conf import settings
from .decorator.services_decorator import BaseRental, HelmetAddon, JacketAddon
from .models import Rental
from vehicles.models import Vehicle
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


def start_rental(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == "POST":
        start = request.POST.get("start_date")
        end = request.POST.get("end_date")
        addons = request.POST.getlist("addons")

        rental = Rental.objects.create(
            user=request.user,
            vehicle=vehicle,
            start_date=start,
            end_date=end,
            addons={"selected": addons},
            status="awaiting_deposit"
        )

        return redirect("rental:deposit", rental.id)

    return render(request, "rentals/rental_start.html", {"vehicle": vehicle})

def deposit(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)

    # calculate charges
    base_price = rental.vehicle.price_per_day
    start = rental.start_date
    end = rental.end_date
    days = (end - start).days or 1

    rental_cost = base_price * days
    decorated = BaseRental(rental_cost)

    addons_selected = rental.addons.get("selected", [])

    if "helmet" in addons_selected:
        decorated = HelmetAddon(decorated, 50000)
    if "jacket" in addons_selected:
        decorated = JacketAddon(decorated, 75000)

    total = decorated.cost()

    context = {
        "rental": rental,
        "days": days,
        "base_total": rental_cost,
        "addons_total": total - rental_cost,
        "grand_total": total,
    }

    if request.method == "POST":

        deposit_amount = request.POST.get("deposit")
        sim_file = request.FILES.get("sim")

        if not deposit_amount or not sim_file:
            context["error"] = "Deposit dan upload SIM wajib."
            return render(request, "rentals/deposit_upload.html", context)

        # save
        rental.deposit_amount = deposit_amount
        rental.sim_image = sim_file
        rental.status = "awaiting_verification"
        rental.save()

        return redirect("rental:pending", rental.id)

    # GET request → render page
    return render(request, "rentals/deposit_upload.html", context)


def pending(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    return render(request, "rentals/pending.html", {"rental": rental})

@staff_member_required
def admin_transactions(request):
    rentals = Rental.objects.all().order_by("-id")
    return render(request, "rentals/admin_transactions.html", {"rentals": rentals})

@login_required
def user_transactions(request):
    rentals = Rental.objects.filter(user=request.user).order_by("-id")
    return render(request, "rentals/user_transactions.html", {"rentals": rentals})
