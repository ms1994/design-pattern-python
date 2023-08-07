"""
    Fichero para crear una shallow copy de una clase
"""

from prototype_interface import IPrototype

class ShallowPrototype(IPrototype):
    """
        COncrete class que crea una shallow copy de esta clase
    """
    def __init__(self, integer = 1, string = '', list = [], dict = {}):
        # Inicializamos la creacion del objeto
        self.integer = integer
        self.string = string
        self.list = list
        self.dict = dict
    
    def clone(self):
        """
            Crea una instance de la clase y la copia
        """
        return type(self)(
            self.integer,
            self.string,
            self.list.copy(),
            self.dict.copy()
        )

    def __str__(self):
        """
            Cambiamos la forma de representar la clase
        """
        ids = id(self)
        return "La clase shallow %s tiene integer = %s, string = %s, list = %s, y dict = %s" % (
                                  ids, self.integer, self.string, self.list, self.dict
        )