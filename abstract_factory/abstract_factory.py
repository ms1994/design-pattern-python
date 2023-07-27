"""
    El abstract factory devuelve una instancia a una factoria
"""
from chair_factory import FactoryChair
from table_factory import FactoryTable
from abc import ABCMeta, abstractstaticmethod

class InterfaceFactoryFurniture(metaclass= ABCMeta):
    """
        Interface para la factoria, la factoria heredara estos metodos.
    """

    @ abstractstaticmethod
    def get_furniture(furnitureType):
        """
            Abstract metodo para desarrollar en el child class, devuelve una factoria (mesa o silla) dependiendo del tipo de furniture
        """

class FurnitureFactory(InterfaceFactoryFurniture):
    """
        Child class del interface donde realmente se ejecutara el codigo para instanciar diferentes factorias
    """

    @ staticmethod
    def get_furniture(furniture_type):
        """
            Codigo para saber que class factory utilizar

            :Params furniture_type: Identificador para saber que clase de factory utilizar
            :Type furniture_type: str

            :Return Instance de la fabrica 
        """
        # Silla factory
        if furniture_type in ['SillaGrande','SillaMediana', 'SillaChiquita']:
            return FactoryChair.get_chair(furniture_type)
        
        # Table factory
        if furniture_type in ['MesaGrande', 'MesaMediana', 'MesaChiquita']:
            return FactoryTable.get_table(furniture_type)

        return None