"""
    Sirve para encapsular diferentes objetos que interactuan entre si, todos los objetos deben interactuar dentro
    del mediator.
"""

from abc import ABCMeta, abstractstaticmethod

class IComponent(metaclass=ABCMeta):

    @abstractstaticmethod
    def notify(msg):
        """
            Abstract method to notify another components
        """
    @abstractstaticmethod
    def receive(msg):
        """
            Abstract method to indicate when a notify is run by a component
        """