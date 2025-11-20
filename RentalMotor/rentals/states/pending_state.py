from .base_state import RentalState

class PendingState(RentalState):
    def approve(self, rental):
        rental.status = "approved"
        rental.vehicle.status = "rented"
        rental.vehicle.save()
        rental.save()

    def reject(self, rental):
        rental.status = "rejected"
        rental.save()

    def complete(self, rental):
        pass
