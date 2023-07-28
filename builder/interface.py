from abc import ABCMeta, abstractstaticmethod

class IHouseBuilder(metaclass=ABCMeta):
    """
        Interface para construir una casa.
    """

    @abstractstaticmethod
    def set_wall_material(self, value):
        """
            Funcion abstract para crear un valor para la pared.
        """

    @abstractstaticmethod
    def set_building_type(self, value):
        """
            Abstract function para asignar un tipo al edificio.
        """

    @abstractstaticmethod
    def set_number_doors(self, value):
        """
            Abstract function para asignar un numero de puertas al constructor
        """

    @abstractstaticmethod
    def set_number_windows(self, value):
        """
            Abstract function para asignar un numero de ventanas al constructor
        """

    @abstractstaticmethod
    def get_result(self):
        """
            Abstract function para construir (builder) la casa.
        """