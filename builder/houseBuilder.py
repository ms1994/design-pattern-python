"""
    Archivo que hereda la interface y crea un tipo de casa en particular con los metodos del builder
"""
import re
from interface import IHouseBuilder
from house_product import House
class HouseBuilder(IHouseBuilder):
    """
        clase para construir una casa (tipo especial de objeto)
        
    """

    def __init__(self):
        # Inicializamos el product  class de la forma
        #self.product = Product()
        self.house = House()

    def set_wall_material(self, value):
        self.house.wall_material = value
        return self

    def set_building_type(self, value):
        """
            Asigna un valor al building
        """
        self.house.building_type = value
        return self

    def set_number_doors(self, value):
        """
            Numero de puertas a la casa a construir
        """

        self.house.doors = value

        return self
    
    def set_number_windows(self, value):
        """
            Numero de ventanas a la casa a construir
        """

        self.house.windows = value
        return self
    
    def get_result(self):
        """
            Devuelve la casa contruida
        """
        return self.house