"""
    Director para construir un tipo de casa
    
"""
from houseBuilder import HouseBuilder

class IglooHouse:

    @staticmethod
    def construct():
        """
            El builder design pattern tiene un director que solo tiene el metodo construct el cual construye un complex object
            por partes, en el orden que quiera usando o repitiendo las partes que quiera
        """

        return HouseBuilder().set_building_type('Igloo')\
                .set_wall_material('Ice').set_number_doors(2)\
                    .set_number_windows(2).get_result()