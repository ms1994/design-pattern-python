from abc import ABCMeta, abstractstaticmethod

class AInterface(metaclass=ABCMeta):

    """
        Interface de alguna clase cualquiera A
    """

    @abstractstaticmethod
    def method_a(self):
        """
            Abstract method de alguna clase A.
        """