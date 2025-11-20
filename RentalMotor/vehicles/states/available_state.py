from .base_state import VehicleState

class AvailableState(VehicleState):
    def available(self, vehicle): 
        pass

    def maintenance(self, vehicle):
        vehicle.status = "maintenance"
        vehicle.save()
