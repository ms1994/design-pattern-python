"""
    Abstract claro que tendra el execute, tambien puede tener el undo o un historial de las acciones que se llevan e ir ejecutando
    su contraria
"""
from abc import ABCMeta, abstractstaticmethod

class ICommand(metaclass=ABCMeta):

    # Static abstract method execute, lo implementaran las child class
    @abstractstaticmethod
    def execute():
        pass