from .pending_state import PendingState
from .approved_state import ApprovedState
from .rejected_state import RejectedState

def get_state(status):
    if status == "awaiting_verification":
        return PendingState()
    if status == "approved":
        return ApprovedState()
    if status == "rejected":
        return RejectedState()
    return PendingState()
