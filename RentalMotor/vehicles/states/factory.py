from .maintenance_state import MaintenanceState
from .available_state import AvailableState

def get_state(status):
    if status == "available":
        return AvailableState()
    if status == "maintenance":
        return MaintenanceState()

    return AvailableState()
