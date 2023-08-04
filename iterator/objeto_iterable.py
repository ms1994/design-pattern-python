from iterator import IIterator

class Iterable(IIterator):

    def __init__(self):
        self.index = 0
        self.max = 7

    def next(self):
        """
            Obtiene el siguiente elemento
        """
        if self.index < self.max:
            x = self.index
            self.index += 1
            return x
        else:
            raise Exception("Indice fuera de rango")

    def has_next(self):
        """
            Metodo para saber si tiene el siguiente
        """
        return self.index < self.max