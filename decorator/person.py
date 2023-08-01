
class Person():
    """
        Clase que inicializa una persona
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_persona(self):
        return "%s tiene %s años de edad" % (self.name, self.age)

