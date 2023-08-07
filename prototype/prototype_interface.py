"""
    Prototype interface, parent class la cual los objetos iran a referenciar para crear un shallow copy
    de una clase o un deep copy.

"""
from abc import ABCMeta, abstractstaticmethod
class IPrototype(metaclass=ABCMeta):
    """
        Interface para los prototipos
    """

    @abstractstaticmethod
    def clone():
        """
            Metodo de clonacion puede ser un shallow copy o deep copy, depende de como lo quieras usasr.
        """

