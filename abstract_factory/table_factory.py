from abc import abstractstaticmethod, ABCMeta

class InterfaceTable(metaclass = ABCMeta):

    """
        Interface para la Table factory, todas las demas clases se heredaran de esta
    """

    @ abstractstaticmethod
    def get_dimensions():
        """
            Este metodo lo implementaran los hijos de esta clase
        """


class BigTable(InterfaceTable):
    """
        1ra clase hija de la interface
    """
    def __init__(self):
        self.heigh = 80 + 40
        self.width = 120 + 40
        self.deep = 50 + 40

    def get_dimensions(self):
        return "La grandes mesas miden %s de alto, %s de ancho y tienen un profundidad de %s" % (self.heigh, self.width, self.deep)


class MediumTable(InterfaceTable):
    """
        2da hija de la interface
    """

    def __init__(self):
        self.heigh = 50 + 20
        self.width = 80 + 20
        self.deep = 30 + 20

    def get_dimensions(self):
        return "Las mesas medianas miden %s de alto, %s de ancho y tienen un profundidad de %s" % (self.heigh, self.width, self.deep)


class SmallTable(InterfaceTable):
    """
        Tercera hija de la interface
    """
    
    def __init__(self):
        self.heigh = 30 + 10
        self.width = 40 + 10
        self.deep = 10 + 10

    def get_dimensions(self):
        return "Las mesas chiquitititas miden %s de alto, %s de ancho y tienen un profundidad de %s" % (self.heigh, self.width, self.deep)

class FactoryTable(InterfaceTable):
    """
        Factoria de mesas, devuelve una instancia a la respectiva mesa, dependiendo del parametro solicitado
    """

    @staticmethod
    def get_table(tableType):
        """
            Funcion para devolver la instancia de una mesa (grande, mediana o small)
            
            :Params tableType: table type sera el indicador que me ayudara a decidir cual instancia devolvera
            :Type tableType: Interfacetable

            Return instance del Interfacetable (uno de sus hijos)

        """

        if tableType == 'MesaGrande':
            return BigTable()

        if tableType == 'MesaMediana':
            return MediumTable()

        if tableType == 'MesaChiquita':
            return SmallTable()

        return None