from context_interfac import IContext
from state import UnpaidState, PaidState, ShippedState, DeliveredState
"""
    All the state change will be handled appropiate by the state design pattern (state object)
"""

class Context(IContext):
    
    def __init__(self) -> None:
        """
            Context should have all the reference to the states
        """ 
        self.unpaid_state = UnpaidState(self)
        self.paid_state = PaidState(self)
        self.shipped_state = ShippedState(self)
        self.delivered_state = DeliveredState(self)

        # Initializer the state in one that dont have anything change yet.
        self.state = self.unpaid_state

    def set_state(self, state):
        self.state = state

    def ship(self):
        self.state.ship()


    def receive_payment(self):
        self.state.receive_payment()

    def mark_delivered(self):
        self.state.mark_delivered()