from singleton_interface import ISingleton

class SingletonPerson(ISingleton):
    """
        Concrete class que ejecuta el singleton, usamos un indicador para saber si ya el singleton
        ha sido instanciado
    """

    __instance = None
    
    
    def get_instance(self):

        if self.__instance is None:
            name = 'Default name'
            age = 10
            SingletonPerson(name, age)

        else:
            return self.__instance

    
    def __init__(self, name, age) -> None:
        """
            Constructor del person singleton
            :Params name: nombre de la persona
            :Type name: str

            :Params age: edad de la persona
            :Type age: int
        """

        if self.__instance is not None:
            raise Exception("Cannot be another instance of singleton")

        self.name = name
        self.age = age
        SingletonPerson.__instance = self

    
    def print_instance(self):
        """
            Print el singleton
        """

        print(f"The person {self.__instance.name} is {self.__instance.age} old")