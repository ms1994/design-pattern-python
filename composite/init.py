"""Fichero para iniciar la prueba del composite design pattern
    El composite desing trata de crear una macro clase que puede tener otras subclases y todas ejecutan
    las mismas operaciones de la clase madre, pudiendo manejar las subclases instance dentro del codigo
    Sirve para crear clases especiales de una interface, las funciones principales son abstract y se definen
    en el interface, todos sus hijos heredaran estas funciones y los hijos que contengan otros hijos pueden
    crear sus propias funciones para manejor las leaves (hijos del hijo, como la funcion agregar departamentos)
"""

from development import DevelopmentDepartment
from account import AccountDepartment
from gran_department import GranDepartment

if __name__ == '__main__':

    # Llamamos a los hijos de la clase departamento, cada hijo representa una historia diferente
    departamento1 = DevelopmentDepartment(235)

    departamento2 = AccountDepartment(124)

    gran_departamento = GranDepartment(32)

    # Funcion especial de una clase macro donde suma las subinstance de las leaves que serian los department unicos
    gran_departamento.agregar_departamentos(departamento1)
    gran_departamento.agregar_departamentos(departamento2)

    # Funcion heredada de la clase madre donde print cada valor de las leaves, mas el total dentro de ellas y todos los hijos
    gran_departamento.print_departamentos()
