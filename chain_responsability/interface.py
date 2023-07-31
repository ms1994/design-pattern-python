from abc import ABCMeta, abstractstaticmethod

class IChain(metaclass = ABCMeta):

    """
        Interface para la clase chain of responsability

        tendra solo los metodos handle y next
    """

    @abstractstaticmethod
    def handle(amount):
        """
            Handle the request (in this example is an amount of money, can have a id to know what handle has to execute)
        """

    @abstractstaticmethod
    def set_successor(successor):
        """
            Set the next chain object, (may has a id to identify what handle use)
        """