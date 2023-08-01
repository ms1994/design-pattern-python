from abc import abstractmethod, ABCMeta

class IDepartment(metaclass = ABCMeta):
    """
        Interface donde se crearan los metodos que manejaran los child class
    """

    @abstractmethod
    def __init__(self, empleados):
        """El codigo se implementara en los child class"""

    @staticmethod
    @abstractmethod
    def print_departamentos():
        """El codigo se implementara en los child class"""
