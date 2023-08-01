from person import Person

class DecoratorPerson(Person):
    """
        Decorator para saber si una persona es un menor, adolescente, adulto o viejo
    """

    def __init__(self, person):
        self._persona = person

    def __getattr__(self, name: str):
        """ Reeditamos el getattr porque nuestro contructor tiene es una persona, entonces si alguien quiere saber
            un atributo de la persona como tal (name, age), utilizando el decorator, ps lo sobreescribimos para enviarle
            esa propiedad desde el person instance
        """
        return getattr(self._persona, name)

    def calcular_edad(self):
        edad = self._persona.age
        estado = 'bebe'
        if edad > 3 and edad < 10:
            estado = 'niño'
        elif edad < 20 and edad >=10:
            estado = 'adolescente'
        elif edad < 60 and edad >=20:
            estado = 'adulto'
        elif edad >= 60:
            estado = 'viejo'

        return ('%s por lo que se le consideraria un %s' % (self._persona.print_persona(), estado))
