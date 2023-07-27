from abc import ABCMeta, abstractstaticmethod

class BInterface(metaclass=ABCMeta):

    """
        Interface de alguna clase cualquiera B
    """

    @abstractstaticmethod
    def method_b(self):
        """
            Abstract method de alguna clase B.
        """