from .base_state import RentalState

class ApprovedState(RentalState):
    def complete(self, rental):
        rental.status = "completed"
        rental.vehicle.status = "available"
        rental.vehicle.save()
        rental.save()

    def approve(self, rental): pass
    def reject(self, rental): pass
