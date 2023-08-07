"""
    Interface for observer objects.
"""
from abc import ABCMeta, abstractstaticmethod

class IObserver(metaclass = ABCMeta):

    """
        Interface for observer objects
    """

    @abstractstaticmethod
    def notify(observable, *args, **kwargs):
        """
            Method abstract to notify when a subject has made a change.
        """