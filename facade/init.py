"""
    El facade design pattern consiste en tener una sola clase que englobe varias, y poder crear metodos en esta clase
    para realizar operaciones en conjunto de todas las demas clases, es como usar otro main(), pero creando metodos para 
    que en el main solo se llamen esos metodos sin mucha complejidad

"""

from facade import Facade


if __name__ == '__main__':

    fac = Facade()
    # Usamos un metodo del facade para hacer un tipo de operacion
    fac.usar_metodo()

    # Usamos otro metodo
    fac.otro_metodo()

    # Y podemos ejecutar complex method
    fac.varios_metodos()