# from strategies import DailyStrategy, HourlyStrategy
# from RentalMotor.rentals.models import Booking, Transaction
# from decimal import Decimal
# from RentalMotor.rentals.decorator.services_decorator import BaseRental, HelmetAddon, DamageFineDecorator

# def create_booking(user, vehicle, start, end, deposit=Decimal('0'), guarantee_doc=''):
#     booking = Booking.objects.create(user=user, vehicle=vehicle, start=start, end=end,
#                                      deposit=deposit, guarantee_doc=guarantee_doc)
#     # mark vehicle as tentatively reserved (business rule)
#     vehicle.status = 'pending'  # or 'reserved' if you want
#     vehicle.save()
#     return booking

# def compute_estimated_price(booking, strategy=DailyStrategy()):
#     return strategy.calculate(booking.vehicle, booking.start, booking.end)

# def finalize_return(booking, user_confirmed, staff_confirmed, damage_amount=None, addons=None):
#     base_price = compute_estimated_price(booking)
#     rental = BaseRental(base_price)
#     # apply addons from addons list (e.g., helmet)
#     if addons:
#         for a in addons:
#             if a.code == 'HELMET': rental = HelmetAddon(rental, a.price)
#     # apply damage
#     if damage_amount:
#         rental = DamageFineDecorator(rental, Decimal(damage_amount))
#     total = rental.cost()
#     tx, _ = Transaction.objects.get_or_create(booking=booking)
#     tx.total = total
#     tx.fines = damage_amount or 0
#     tx.user_confirmed = user_confirmed or tx.user_confirmed
#     tx.staff_confirmed = staff_confirmed or tx.staff_confirmed
#     if tx.user_confirmed and tx.staff_confirmed:
#         tx.finalized = True
#         booking.status = 'returned'
#         booking.vehicle.status = 'available'
#         booking.vehicle.save()
#         booking.save()
#     tx.save()
#     return tx
