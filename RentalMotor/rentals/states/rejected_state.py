from .base_state import RentalState

class RejectedState(RentalState):
    def approve(self, rental): pass
    def reject(self, rental): pass
    def complete(self, rental): pass
