"""
    Fichero para crear una deep copy de una clase
"""

from prototype_interface import IPrototype
import copy

class DeepPrototype(IPrototype):
    """
        COncrete class que crea una Deep copy de esta clase
    """
    def __init__(self, integer = 1, string = '', list = [], dict = {}):
        # Inicializamos la creacion del objeto
        self.integer = integer
        self.string = string
        self.list = list
        self.dict = dict
    
    def clone(self):
        """
            Crea una instance de la clase y la copia (deep usando el copy module)
        """
        return type(self)(
            self.integer,
            self.string,
            copy.deepcopy(self.list),
            copy.deepcopy(self.dict)
        )

    def __str__(self):
        """
            Cambiamos la forma de representar la clase
        """
        ids = id(self)
        return "La clase Deep %s tiene integer = %s, string = %s, list = %s, y dict = %s" % (
                                  ids, self.integer, self.string, self.list, self.dict
        )