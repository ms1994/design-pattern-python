"""
    Fichero que crea la clase del producto
"""

class House():

    def __init__(self, building_type = 'General', wall_material = 'concreto', doors = 0, windows = 0):
        """
            Crea el producto y lo dividimos en las partes que queremos construir, lo podemos dividir las partes que queramos
            y se crea un metodo en el interface para cada parte del product
        """

        self.building_type = building_type
        self.wall_material = wall_material
        self.doors = doors
        self.windows = windows


    def __str__(self) -> str:
        return "Esta casa de tipo %s, tiene paredes de %s y %s puertas con %s ventanas" % (self.building_type,
                                                    self.wall_material, self.doors, self.windows)