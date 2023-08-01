"""
    Decorator pattern sirve para darle funcionalidad a una clase, su objetivo es hacerlo en runtime, y utiliza
    una instance de la clase a modificar como dato, luego ejecuta una serie de funciones con base a esta instancia
    ocasionando mas funcionalidad a esta misma, todos los decorator deben heredar la clase en estudio
"""

from person import Person
from decoratorPerson import DecoratorPerson

if __name__ == '__main__':
    # Creamos a las personas
    p1 = Person('Juno', 1)
    p2 = Person('Carmen', 61)
    p3 = Person('Lino', 58)
    p4 = Person('Angee', 19)
    p5 = Person('Miquel', 8)

    personas = []
    # Guardamos las personas en una lista de personas
    personas.append(p1)
    personas.append(p2)
    personas.append(p3)
    personas.append(p4)
    personas.append(p5)

    # Si quisiera de repente saber si las personas son adultas o ninos para futuras funciones aplico mi decorator
    for persona in personas:
        # Inicializamos el decoretor design con la persona
        decorator = DecoratorPerson(persona)
        # Ejecutamos la funcion del decorator para agregarle funcionalidad en base a la persona enviada
        print(decorator.calcular_edad())
    
