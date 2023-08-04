"""
    El iterator design lo que hace es crear un interface donde las clases puedan ser iterables sin importar si
    el objeto es una lista, un dict, array lo que sea. En lenguaje como java o c++ se transforma el objeto a iterar en
    un pointer y se viaja a traves de el usando pointer, asi podremos viajar por cualquier tipo de estructura.

    El iterator design es la abstract class, en python por ejm se implementa los metodo de next y has_next y en base a esos
    metodos se adaptaran los child class y sus atributos para coincider con cada metodo, el next debe retornar el siguiente valor
    del atributo empezando por el primero, y el has_next indica cuando parar. 
"""

from objeto_iterable import Iterable

if __name__ == '__main__':
    objeto_ite = Iterable()

    while objeto_ite.has_next():
        print(objeto_ite.next())