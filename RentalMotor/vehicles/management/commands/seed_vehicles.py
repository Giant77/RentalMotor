# vehicles/management/commands/seed_vehicles.py

from django.core.management.base import BaseCommand
from vehicles.models import Vehicle
from decimal import Decimal


class Command(BaseCommand):
    help = "Seed dummy vehicles"

    def handle(self, *args, **kwargs):

        Vehicle.objects.all().delete()

        data = [
            {
                "plate": "BK1234AA",
                "make": "Honda",
                "model": "Vario 125",
                "year": 2022,
                "price_per_day": Decimal("65000"),
                "status": "available",
                "notes": "Unit standar",
                "tnc": "Harus memiliki SIM C"
            },
            {
                "plate": "BL9876BB",
                "make": "Yamaha",
                "model": "NMAX 155",
                "year": 2023,
                "price_per_day": Decimal("90000"),
                "status": "available",
                "notes": "Cocok perjalanan jauh",
                "tnc": "Deposit wajib"
            },
            {
                "plate": "BK1122CC",
                "make": "Suzuki",
                "model": "Beat Street",
                "year": 2021,
                "price_per_day": Decimal("60000"),
                "status": "maintenance",
                "notes": "Perlu pengecekan rem",
                "tnc": "Tidak dapat disewa sementara"
            },
            {
                "plate": "BL3344DD",
                "make": "Honda",
                "model": "Scoopy",
                "year": 2020,
                "price_per_day": Decimal("70000"),
                "status": "rented",
                "notes": "Sedang disewa",
                "tnc": "Kembali besok"
            },
            {
                "plate": "BK5566EE",
                "make": "Yamaha",
                "model": "Aerox 155",
                "year": 2022,
                "price_per_day": Decimal("95000"),
                "status": "available",
                "notes": "Unit sporty",
                "tnc": "Dilarang kebut-kebutan"
            }
        ]

        for item in data:
            Vehicle.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Dummy vehicle data seeded"))
