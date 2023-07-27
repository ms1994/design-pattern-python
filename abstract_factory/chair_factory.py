from abc import abstractstaticmethod, ABCMeta

class InterfaceChair(metaclass = ABCMeta):

    """
        Interface para la chair factory, todas las demas clases se heredaran de esta
    """

    @ abstractstaticmethod
    def get_dimensions():
        """
            Este metodo lo implementaran los hijos de esta clase
        """


class BigChair(InterfaceChair):
    """
        1ra clase hija de la interface
    """
    def __init__(self):
        self.heigh = 80
        self.width = 120
        self.deep = 50

    def get_dimensions(self):
        return "La grandes silla miden %s de alto, %s de ancho y tienen un profundidad de %s" % (self.heigh, self.width, self.deep)


class MediumChair(InterfaceChair):
    """
        2da hija de la interface
    """

    def __init__(self):
        self.heigh = 50
        self.width = 80
        self.deep = 30

    def get_dimensions(self):
        return "La sillas medianas miden %s de alto, %s de ancho y tienen un profundidad de %s" % (self.heigh, self.width, self.deep)


class SmallChair(InterfaceChair):
    """
        Tercera hija de la interface
    """
    
    def __init__(self):
        self.heigh = 30
        self.width = 40
        self.deep = 10

    def get_dimensions(self):
        return "La sillas chiquitititas miden %s de alto, %s de ancho y tienen un profundidad de %s" % (self.heigh, self.width, self.deep)

class FactoryChair(InterfaceChair):
    """
        Factoria de sillas, devuelve una instancia a la respectiva silla, dependiendo del parametro solicitado
    """

    @staticmethod
    def get_chair(chairType):
        """
            Funcion para devolver la instancia de una silla (grande, mediana o small)
            
            :Params chairType: Chair type sera el indicador que me ayudara a decidir cual instancia devolver4
            :Type chairType: InterfaceChair

            Return instance del InterfaceChair (uno de sus hijos)

        """

        if chairType == 'SillaGrande':
            return BigChair()

        if chairType == 'SillaMediana':
            return MediumChair()

        if chairType == 'SillaChiquita':
            return SmallChair()

        return None