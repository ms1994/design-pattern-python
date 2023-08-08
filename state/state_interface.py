"""
    Interface of the state design pattern, should have the same method that the context interface
"""

from abc import ABCMeta, abstractstaticmethod

class IState(metaclass=ABCMeta):

    @abstractstaticmethod
    def ship():
        """Abstrac method ship"""

    @abstractstaticmethod
    def receive_payment():
        """Abstract received payment"""

    @abstractstaticmethod
    def mark_delivered():
        """Abstract method of delivered"""