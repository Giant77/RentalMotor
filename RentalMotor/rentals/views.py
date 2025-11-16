from django.shortcuts import render, get_object_or_404, redirect
from vehicles.models import Vehicle
from .models import Rental
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def start_rental(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == "POST":
        start = request.POST.get("start_date")
        end = request.POST.get("end_date")
        addons = request.POST.getlist("addons")

        r = Rental.objects.create(
            user=request.user,
            vehicle=vehicle,
            start_date=start,
            end_date=end,
            addons={"selected": addons},
            status="awaiting_deposit"
        )

        return redirect("rental:deposit", r.id)

    return render(request, "rentals/rental_start.html", {"vehicle": vehicle})

def deposit(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)

    if request.method == "POST":
        rental.deposit_amount = request.POST.get("deposit")
        rental.sim_image = request.FILES.get("sim")
        rental.status = "awaiting_verification"
        rental.save()

                # Notify all admins via email
        admins = User.objects.filter(is_superuser=True).values_list("email", flat=True)
        send_mail(
            subject="Rental Pending Verification",
            message=f"Rental ID {rental.id} from {rental.user.username} is awaiting verification.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=list(admins),
            fail_silently=True,
        )

        return redirect("rentals/rental:pending", rental.id)

    return render(request, "rentals/deposit_upload.html", {"rental": rental})

def pending(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    return render(request, "rentals/pending.html", {"rental": rental})
