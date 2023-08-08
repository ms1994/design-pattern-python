from abc import ABCMeta, abstractstaticmethod

class ISingleton(metaclass=ABCMeta):
    """
        Abstract interface para la clase singleton
    """

    
    @abstractstaticmethod
    def get_instance():
        """
            Interface to implement in the child component
        """

    @abstractstaticmethod
    def print_instance():
        """
            Interface to implement in the child component
        """
