"""
    El singleton asegura solo una instancia de la clase, se usa utilizando un indicador que nos dice
    si ya ha sido instanciado o no.
"""
from singleton import SingletonPerson
if __name__ == '__main__':

    p = SingletonPerson('Miquel', 25)

    p.print_instance()
    print("P1", p)
    
    # Si quieres usar otra variable debes llamar al metodo get_instance y asi evita la creacion de otro singleton
    p2 = p.get_instance()

    # Print el mismo person Singleton 
    p2.print_instance()