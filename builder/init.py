"""
    El builder desing patter te permite construir complex object utilizando el contruct method en el director
    donde puedes decidir como construir tu objeto, si tener dos partes o tres partes y asi.

    El usuario solo tendra que llamar al construct especifico por el tipo de objeto que quiere, asi puedes crear
    varios tipos de objeto de una misma familia con diferentes propiedades y atributos.

    Los director class retornan el producto, que esta hecho segun las especificaciones de nuestro director.
"""

from igloo_director import IglooHouse
from house_director import HouseWooden

if __name__ == '__main__':

    igloo = IglooHouse.construct()

    print("Igloo", igloo)

    woden_house = HouseWooden.construct()

    print("Wooden house",woden_house)