from .base_state import VehicleState

class MaintenanceState(VehicleState):
    def available(self, vehicle): 
        vehicle.status = "available"
        vehicle.save()


    def maintenance(self, vehicle):
        pass
