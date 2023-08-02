from classA import A
from classB import B

class Facade:

    _objecto_1 = None
    _objeto_2 = None
    def __init__(self):
        """
            Puedes iniciar la clase como tu quieras y utilizar los objetos que quieras
        """

        self._objecto_1 = A()
        self._objeto_2 = B()


    def usar_metodo(self):
        """
            Funcion sencilla de leer y utilizar por el usuario para ejecutar una seria de complejas operacioes
            usando otras clases e interacciones entre ellas
        """

        res = self._objecto_1.some_method()
        print("Se ejecuta el objeto 1, %s" % res)

    def otro_metodo(self):
        res = self._objeto_2.some_method_b()
        print("Otra metodo %s" % res)

    def varios_metodos(self):
        """
            Ejecutamos varios metodos
        """

        res1 = self._objecto_1.some_method()

        res2 = self._objeto_2.some_method_b()

        print("Complejidad %s con %s" % (res1, res2))
