"""File that are going to have all the different state, you can make one file for all the different state class or a
unique file that containt all the classes, for simplicity we all going to make all in this file.
"""

from state_interface import IState

class UnpaidState(IState):

    def __init__(self, context) -> None:
        """
        Params context: context object
        """
        self.context = context

    def receive_payment(self):
        # In the unpaid state the receive_payment change our state to paid_state
        self.context.set_state(self.context.paid_state)
        print("Dinero recibido")

    def ship(self):
        print("Primero debes recibir el dinero")

    def mark_delivered(self):
        print("Primero debes recibir el dinero")

class PaidState(IState):

    def __init__(self, context) -> None:
        """
        Params context: context object
        """
        self.context = context

    def receive_payment(self):
        print("Ya esta pagado")

    def ship(self):
        print("Shipping your product siiiuuuu!!")
        self.context.set_state(self.context.shipped_state)

    def mark_delivered(self):
        print("Only shipped state can mark delivered")

class ShippedState(IState):

    def __init__(self, context) -> None:
        """
        Params context: context object
        """
        self.context = context

    def receive_payment(self):
        print("Ya esta pagado, y se esta empaquetando para enviar")

    def ship(self):
        print("No, producto ya fue enviado")
        
    def mark_delivered(self):
        print("Product is here yeahhh!!!!")
        self.context.set_state(self.context.delivered_state)

class DeliveredState(IState):


    def __init__(self, context) -> None:
        """
        Params context: context object
        """
        self.context = context

    def receive_payment(self):
        print("Ya esta pagado, enviado y recibido en las manos del usuario")

    def ship(self):
        print("Ya esta pagado, enviado y recibido en las manos del usuario")

    def mark_delivered(self):
        print("Ya esta pagado, enviado y recibido en las manos del usuario")
