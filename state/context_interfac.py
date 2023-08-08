from abc import ABCMeta, abstractstaticmethod

class IContext(metaclass = ABCMeta):
    """
        Interface for the context class (class to handle the change of the states)
    """

    @abstractstaticmethod
    def ship():
        """
            Do the shipment.
        """

    @abstractstaticmethod
    def receive_payment():
        """
            Receive the payment
        """

    @abstractstaticmethod
    def mark_delivered():
        """
            Mark the delivered state
        """