"""
    Otro tipo de caso, con su director predeterminado
"""

from houseBuilder import HouseBuilder

class HouseWooden:

    @staticmethod
    def construct():
        """
            El builder design pattern tiene un director que solo tiene el metodo construct el cual construye un complex object
            por partes, en el orden que quiera usando o repitiendo las partes que quiera
        """

        return HouseBuilder().set_building_type('Wooden')\
                .set_wall_material('Wood').set_number_doors(4)\
                    .set_number_windows(3).get_result()