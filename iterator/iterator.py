from abc import ABCMeta, abstractstaticmethod

class IIterator(metaclass=ABCMeta):
    """
        Interface para el iterator
    """
    @abstractstaticmethod
    def next():
        """
            Abstract method que implementara la child class
        """
        pass

    @abstractstaticmethod
    def has_next():
        """
            Abstract method que implementara la child class
        """
        pass
